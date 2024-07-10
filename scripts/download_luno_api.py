import asyncio

from playwright.async_api import async_playwright


async def download_file():
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the page
        await page.goto("https://www.luno.com/en/developers/api")

        # Wait for the download button to be available
        await page.wait_for_selector("a.sc-bsatvv.gidAUi")

        # Get the download button element
        download_button = await page.query_selector("a.sc-bsatvv.gidAUi")

        # Click the download button and intercept the request
        async with page.expect_download() as download_info:
            await download_button.click()

        # Wait for the download to complete
        download = await download_info.value

        save_to = "specs/luno_openapi.json"
        # Save the downloaded file
        await download.save_as(save_to)

        print(f"Download completed and saved to {save_to}")
        await browser.close()


# Run the async function
asyncio.run(download_file())
