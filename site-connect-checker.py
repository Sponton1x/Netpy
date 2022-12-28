# __main__.py

import sys, pathlib
from http.client import HTTPConnection
from  urllib.parse import urlparse
import argparse

__version__ = "0.1.0"

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="rpchecker", description="check the online of website"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website urls",
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read urls for a file"
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    print(f"The status of {url} is", end=" ")
    if result:
        print("Online")
    else:
        print(f"Offline \n Error {error}")

def site_is_online(url, timeout=2):
    error = Exception("unknow error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        conection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            conection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            conection.close()
        raise error

def main():
    user_args = read_user_cli_args()
    urls = _get_website_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)

def _get_website_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []

def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()