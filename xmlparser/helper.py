import argparse
def return_args():
    parser = argparse.ArgumentParser(description="XML Product Data parser")
    parser.add_argument('filepath', type=str, help="Please provide the path to the file containing the xml product data")
    args = parser.parse_args()
    return args
