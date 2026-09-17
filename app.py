import os
import sys
import datetime
import logging

# Configure output logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def fetch_system_metrics():
    """Simulate fetching system and database statistics."""
    logging.info("Gathering application state metrics...")
    return {
        "system_status": "HEALTHY",
        "total_registered_users": 1285,
        "active_sessions": 142,
        "database_latency_ms": 12.4,
        "error_rate_percentage": 0.02
    }

def generate_report(file_path="report.txt"):
    """Generates a structured system report file."""
    logging.info("Starting report generation process...")
    metrics = fetch_system_metrics()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(file_path, "w", encoding="utf-8") as report_file:
            report_file.write("===============================================\n")
            report_file.write(" STUDENT MANAGEMENT SYSTEM - SYSTEM REPORT    \n")
            report_file.write("===============================================\n")
            report_file.write(f"Generated On          : {current_time}\n")
            report_file.write(f"System Health Status  : {metrics['system_status']}\n")
            report_file.write("-----------------------------------------------\n")
            report_file.write(f"Total Registered Users: {metrics['total_registered_users']}\n")
            report_file.write(f"Active User Sessions  : {metrics['active_sessions']}\n")
            report_file.write(f"DB Latency (ms)       : {metrics['database_latency_ms']}\n")
            report_file.write(f"Error Rate            : {metrics['error_rate_percentage']}%\n")
            report_file.write("===============================================\n")
            report_file.write("Report Generation Completed Successfully.\n")
        
        logging.info("Report file successfully written to: %s", os.path.abspath(file_path))
    except IOError as err:
        logging.error("Failed to write report file: %s", err)
        sys.exit(1)

if __name__ == "__main__":
    generate_report()