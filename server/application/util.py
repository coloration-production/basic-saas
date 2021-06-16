import aiohttp
import async_timeout
import socket

async def asyncPost (url, params):

  conn = aiohttp.TCPConnector(
    family=socket.AF_INET,
    verify_ssl=False,
  )

  async with aiohttp.ClientSession(connector=conn) as session, async_timeout.timeout(10):
    async with session.post(url, params = params) as response:
      return await response.text()