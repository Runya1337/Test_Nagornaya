import asyncio
import aiohttp
from urllib.parse import urlparse

HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']

def is_valid_url(url):
    """
    Проверяет, является ли заданная строка валидным URL.
    """
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

async def check_method(session, url, method):
    """
    Проверяет, доступен ли заданный HTTP-метод для указанного URL.
    """
    try:
        async with session.request(method, url) as response:
            if response.status != 405:
                return method, response.status
    except Exception:
        pass  # Для простоты игнорируем исключения
    return None

async def process_url(session, url):
    """
    Обрабатывает один URL для определения доступных HTTP-методов.
    """
    tasks = [check_method(session, url, method) for method in HTTP_METHODS]
    responses = await asyncio.gather(*tasks)
    results = {}
    for res in responses:
        if res:
            method, status = res
            results[method] = status
    return url, results

async def check_urls(urls):
    """
    Обрабатывает несколько URL одновременно.
    """
    final_result = {}
    async with aiohttp.ClientSession() as session:
        tasks = [process_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, methods in results:
            if methods:
                final_result[url] = methods
    return final_result
