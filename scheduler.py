"""Script for scheduling jobs with the schedule module."""

import schedule
import time
import argparse

from google_search import GPSE

class scheduler():
    def __init__(self, args) -> None:
        self.args=args

    def job(self):
        googler = GPSE(self.args)
        googler.search_google_endpoints()
        print("Job running")

    def scheduler(self):
        schedule.every(5).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument('--keywords', nargs='*', required=True, help='Keywords to search for')

    # Parse the arguments
    args = parser.parse_args()

    # Run search
    scheduler = scheduler(args)
    scheduler.scheduler()

