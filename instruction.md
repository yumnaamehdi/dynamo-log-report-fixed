Read the web server log stored at `/app/access.log` and generate a summary report at `/app/report.json`.

The report must be a valid UTF-8 encoded JSON object containing only the fields `total_requests`, `unique_ips`, and `top_path`.

Count every non-empty line in the log and store the result in `total_requests`.

Count the number of distinct client IP addresses appearing in the log. The client IP address is the first whitespace-separated value on each non-empty line. Store this result in `unique_ips`.

Determine which URL path appears most frequently in the HTTP requests recorded in the log and store that path as a string in `top_path`.

The report written to `/app/report.json` must contain the values `6` for `total_requests`, `3` for `unique_ips`, and `"/index.html"` for `top_path`.

Do not include any additional fields, comments, explanations, or data outside the JSON object.
