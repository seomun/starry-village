/* Dress Story 서비스 워커 — 앱 셸은 설치 시 캐시, 데이터·이미지는 처음 요청 때 캐시(오프라인 재플레이 가능).
   버전을 올리면(CACHE 이름) 이전 캐시는 activate 때 지운다. */
const CACHE = 'dress-story-v1';
const SHELL = ['./', './index.html', './manifest.webmanifest'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => {
    if (res.ok && new URL(e.request.url).origin === location.origin) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }
    return res;
  }).catch(() => hit)));
});
