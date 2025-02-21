const CACHE_NAME = "tomato-bot-cache-v1";
const urlsToCache = [
    "/",
    "/offline.html",  // Add an offline page
    "/static/style.css",
    "/static/manifest.json",
    "/static/icons/icon-192x192.png",
    "/static/icons/icon-512x512.png"
];

// Install Service Worker and cache resources
self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(urlsToCache))
            .then(self.skipWaiting())
    );
});

// Activate Service Worker and remove old caches
self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) =>
            Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            )
        )
    );
});

// Fetch resources from cache or show offline page
self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request).catch(() => caches.match("/offline.html"));
        })
    );
});
