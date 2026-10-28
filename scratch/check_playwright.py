import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width in [360, 390, 768, 1200]:
            page = await browser.new_page(viewport={'width': width, 'height': 800})
            await page.goto('http://localhost:8080/scratch/preview_dobra10_animated.html')
            # wait 2.5s for animations
            await page.wait_for_timeout(2500)
            
            # Check bounding boxes and overflow
            scroll_width = await page.evaluate('document.documentElement.scrollWidth')
            client_width = await page.evaluate('document.documentElement.clientWidth')
            has_h_scroll = scroll_width > client_width
            
            card_box = await page.locator('.guarantee-card').bounding_box()
            section_box = await page.locator('#guarantee').bounding_box()
            btn_box = await page.locator('.btn-cta').bounding_box()
            
            print(f"Viewport {width}px: scrollWidth={scroll_width}, clientWidth={client_width}, hScroll={has_h_scroll}")
            print(f"  Card: x={card_box['x']:.1f}, width={card_box['width']:.1f}")
            print(f"  Button: x={btn_box['x']:.1f}, width={btn_box['width']:.1f}")
            
            await page.screenshot(path=f'scratch/pw_{width}.png')
        await browser.close()

asyncio.run(run())
