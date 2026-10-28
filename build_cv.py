"""Rebuild cv.pdf from cv.html (run from anywhere: python3 build_cv.py)."""
import asyncio
import pathlib

from playwright.async_api import async_playwright

HERE = pathlib.Path(__file__).resolve().parent


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto((HERE / "cv.html").as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.pdf(path=str(HERE / "cv.pdf"), print_background=True, prefer_css_page_size=True)
        await browser.close()
    print("wrote", HERE / "cv.pdf")


asyncio.run(main())
