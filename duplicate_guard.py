import hashlib
from django.core.cache import cache
from django.http import HttpResponse

class DuplicateGuard(object):

    ENABLED = True
    TIMEOUT = 10

    def process_request(self, request):

        if not self.ENABLED:
            return None

        if request.method != 'POST':
            return None

        body = request.body or str(request.POST)

        raw = "%s:%s" % (request.path, body)

        key = hashlib.md5(raw.encode('utf-8')).hexdigest()
        cache_key = "dup_guard:%s" % key

        if cache.get(cache_key):
            return HttpResponse("Duplicate blocked", status=409)

        cache.set(cache_key, True, self.TIMEOUT)

        return None





    #  PUT IT HERE (IMPORTANT POSITION)   Insert it right before TenantMiddleware.
    # 'smcproject.duplicate_guard.DuplicateGuard',

    # "tenants.middlewares.TenantMiddleware",