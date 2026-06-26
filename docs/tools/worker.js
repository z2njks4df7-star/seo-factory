// Core SEO Factory Service Worker with stale-while-revalidate for HTML
const CACHE_NAME = 'seo-factory-v2';
const PRECACHE_URLS = [
  '/',
  '/tools/immortality-v14.5.html',
  // Inline CSS/JS are inside HTML, no separate files
];

// Install: precache core resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(PRECACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
    )).then(() => self.clients.claim())
  );
});

// Fetch: strategy based on request type
self.addEventListener('fetch', event => {
  const { request } = event;
  // Only handle GET requests
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  // Only same-origin requests
  if (url.origin !== location.origin) return;

  // HTML documents: network-first, fallback to cache, update cache in background
  if (request.destination === 'document' || request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(networkResponse => {
          // Clone and cache the response for offline use
          const responseClone = networkResponse.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
          return networkResponse;
        })
        .catch(() => caches.match(request)) // fallback to cache if network fails
    );
    return;
  }

  // For other assets (scripts, styles, images, etc): cache-first with network update
  event.respondWith(
    caches.match(request)
      .then(cachedResponse => {
        // Return cached version immediately if available
        if (cachedResponse) return cachedResponse;
        // Otherwise fetch from network and cache
        return fetch(request)
          .then(networkResponse => {
            // Don't cache non-success responses or non‑same‑origin
            if (!networkResponse || networkResponse.status !== 200) {
              return networkResponse;
            }
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
            return networkResponse;
          })
          .catch(() => {
            // If network fails, we already returned undefined above; fallback to nothing
            // Could return a fallback image/page if desired
            return Response.error();
          });
      })
  );
});
