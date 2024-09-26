import pytest
from url_checker import is_valid_url, check_urls

@pytest.mark.asyncio
async def test_check_urls():
    # Тестирование с одним валидным URL
    urls = ['https://httpbin.org/']
    result = await check_urls(urls)
    assert 'https://httpbin.org/' in result
    assert 'GET' in result['https://httpbin.org/']
    assert result['https://httpbin.org/']['GET'] == 200

@pytest.mark.asyncio
async def test_check_urls_multiple():
    # Тестирование с несколькими валидными URL
    urls = ['https://httpbin.org/', 'https://example.com']
    result = await check_urls(urls)
    assert len(result) == 2
    assert 'https://httpbin.org/' in result
    assert 'https://example.com' in result

@pytest.mark.asyncio
async def test_check_urls_invalid():
    # Тестирование с недопустимым URL
    urls = ['not a url']
    result = await check_urls(urls)
    assert result == {}

@pytest.mark.asyncio
async def test_check_urls_mixed():
    # Тестирование со смешанными валидными и недопустимыми URL
    urls = ['https://httpbin.org/', 'not a url', 'https://example.com']
    result = await check_urls(urls)
    assert len(result) == 2
    assert 'https://httpbin.org/' in result
    assert 'https://example.com' in result

def test_is_valid_url():
    # Тестирование валидных URL
    assert is_valid_url('https://google.com') == True
    assert is_valid_url('http://example.com') == True
    assert is_valid_url('ftp://example.com') == True  # Поддержка других схем

def test_is_invalid_url():
    # Тестирование недопустимых строк
    assert is_valid_url('not a url') == False
    assert is_valid_url('www.example.com') == False  # Отсутствует схема
    assert is_valid_url('') == False

def test_is_valid_url_edge_cases():
    # Тестирование граничных случаев
    assert is_valid_url('http://') == False
    assert is_valid_url('://example.com') == False
    assert is_valid_url('http:///example.com') == False

@pytest.mark.asyncio
async def test_check_urls_timeout():
    # Тестирование с URL, который может вызвать таймаут
    urls = ['https://10.255.255.1']  # Этот IP обычно недоступен
    result = await check_urls(urls)
    assert result == {}

@pytest.mark.asyncio
async def test_check_urls_unreachable():
    # Тестирование с несуществующим доменом
    urls = ['http://nonexistent.domain.example']
    result = await check_urls(urls)
    assert result == {}
