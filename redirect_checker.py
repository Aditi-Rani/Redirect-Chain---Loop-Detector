import requests

def check_redirects(url):
    try:
        print(f"🔍 Checking redirects for: {url}\n")

        response = requests.get(url, allow_redirects=True, timeout=10)
        history = response.history

        if not history:
            print("✅ No redirects. Page resolves directly.\n")
            return

        print(f"🔁 Total Redirects: {len(history)}")
        print("📜 Redirect Chain:")
        for i, resp in enumerate(history):
            print(f"  {i+1}. {resp.status_code} → {resp.headers['Location']}")

        # Detect potential loop
        final_url = response.url
        if final_url == url:
            print("\n⚠️ Potential redirect loop detected: Final URL is same as the start URL.")
        else:
            print(f"\n✅ Final Destination: {final_url}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = input("🔗 Enter the URL (with https://): ").strip()
    check_redirects(url)
