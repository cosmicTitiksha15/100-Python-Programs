# Scan a log file for specific keywords like "ERROR" or "WARNING".
import os

def search_log_file(input_file, keywords, output_file=None):
    '''
    Scans a log file for specific keywords and prints or saves the matching lines.
    :param input_file: Path to the source log file.
    :param keywords: A list of string keywords to look for (e.g; ["ERROR", "WARNING"])
    :param output_file: Optional path to save the matching results.
    '''

    if not os.path.exists(input_file):
        print(f"❌ Error: The file '{input_file}' does not exist.")
        return
    
    match_count = 0
    out_file = None

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            if output_file:
                out_file = open(output_file, 'w', encoding='utf-8')
                out_file.write(f"--- Log Search Results for '{keywords}' ---\n\n")
            print(f"Scanning {input_file} for {keywords}...")
            print("-" * 50)

            # Read line-by-line(highly memory efficient)
            for line_number, line in enumerate(infile, start=1):
                # Check if any keyword exists in current line.
                if any(keyword in line for keyword in keywords):
                    match_count += 1
                    formatted_line = f"Line {line_number} : {line.strip()}"
                    print(formatted_line)

                    if out_file:
                        out_file.write(formatted_line + "\n")

        print("-" * 50)
        print(f"Scan complete. Found {match_count} matching lines.")

    except Exception as e:
        print(f"An error occured while processing the file. {e}")

    finally:
        if out_file:
            out_file.close()


sample_log = "app_demo.log"
with open(sample_log, "w", encoding="utf-8") as f:
        f.write("2026-06-10 12:00:01 INFO: Server started successfully.\n")
        f.write("2026-06-10 12:05:23 WARNING: High memory usage detected.\n")
        f.write("2026-06-10 12:10:14 INFO: User 'Titiksha' logged in.\n")
        f.write("2026-06-10 12:15:45 ERROR: Database connection failed!\n")
        f.write("2026-06-10 12:20:00 CRITICAL: Out of memory. Shutting down.\n")

search_terms = ["ERROR", "CRITICAL"]
summary_report = "error_report.txt"
search_log_file(sample_log, search_terms, summary_report)