# LinkedIn Job Searcher 🔍

A powerful, comprehensive tool designed to create optimized LinkedIn job search URLs with advanced filtering options. This application automates the LinkedIn URL hacking technique to find jobs posted within precise time frames and custom search criteria.

## 🌟 Key Features

- 🔍 **Advanced URL Building**: Create sophisticated LinkedIn search URLs with all available parameters
- ⏰ **Precision Time Filtering**: Find jobs posted within custom time frames (30 minutes to months)
- 🎯 **Laser-Focused Targeting**: Filter by experience level, job type, location, and remote work options
- 🖥️ **Dual Interface Options**: Both intuitive web UI (Streamlit) and powerful command-line interface
- 📋 **Enhanced Clipboard Support**: One-click URL copying with improved reliability
- 🚀 **Direct LinkedIn Access**: Quick links to open searches directly in LinkedIn
- 🆔 **Job ID Integration**: Manual job ID input for specific job tracking
- 🎨 **Modern UI**: Clean, user-friendly interface with improved styling

## 🚀 Quick Start

### Web Interface (Recommended)

1. **Start the application**:
   ```bash
   python main.py --mode web
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Enter your search criteria** and click the blue "Generate LinkedIn Search URL" button

4. **Copy the URL** with the improved copy button and use it in LinkedIn

### Command Line Interface

**Basic job search**:
```bash
python main.py --mode cli "Python Developer" --location "San Francisco"
```

**Advanced search with multiple filters**:
```bash
python cli.py "Data Scientist" --time "4 hours" --experience mid_senior,director --remote remote,hybrid --distance 50
```

**Quick time-based searches** (LinkedIn URL hacking technique):
```bash
# Jobs posted in last 30 minutes
python cli.py "Software Engineer" --custom-hours 0.5 --sort date_posted

# Jobs posted in last 2 hours
python cli.py "DevOps Engineer" --time "2 hours" --remote remote
```

**With Job ID and Geographic targeting**:
```bash
python cli.py "director sales operations" --location "United States" --time "1 hour" --geo-id 103644278 --job-id 4185657072 --summary
```

### Python Module

```python
from linkedin_url_builder import LinkedInURLBuilder

# Create a URL builder
builder = LinkedInURLBuilder()

# Build a search URL
url = (builder
       .set_keywords("Python Developer")
       .set_location("San Francisco")
       .set_time_filter("24 hours")
       .set_distance(25)
       .set_sort_by("date_posted")
       .set_experience_level(['mid_senior'])
       .set_remote_options(['remote', 'hybrid'])
       .build_url())

print(url)
```

## 📦 Installation

1. **Clone or download the project** to your local machine
2. **Navigate to the project directory**:
   ```bash
   cd linkedin_job_searcher
   ```
3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python main.py --mode web
   ```

## LinkedIn URL Parameters Explained

This tool manipulates LinkedIn's URL parameters to create optimized searches:

- **`keywords`**: Job title, skills, or search terms
- **`location`**: Geographic location or "Remote"
- **`f_TPR`**: Time filter (r3600 = 1 hour, r86400 = 24 hours, etc.)
- **`distance`**: Search radius in miles
- **`sortBy`**: Sort by relevance (R) or date posted (DD)
- **`f_E`**: Experience level filter
- **`f_JT`**: Job type filter (full-time, part-time, contract, etc.)
- **`f_WT`**: Work arrangement (on-site, remote, hybrid)
- **`geoId`**: Precise geographic targeting

## 🎯 LinkedIn URL Hacking Technique

This tool automates the powerful LinkedIn URL manipulation technique for finding jobs posted within precise time frames:

### How It Works:
1. **Time Parameter**: LinkedIn uses `f_TPR=r{seconds}` to filter by posting time
2. **Custom Timing**: Instead of just "24 hours", you can search for jobs posted in the last 30 minutes, 2 hours, etc.
3. **Fresh Opportunities**: Catch new job postings before they get flooded with applications

### Time Conversion Examples:
- **30 minutes**: `f_TPR=r1800`
- **1 hour**: `f_TPR=r3600`
- **4 hours**: `f_TPR=r14400`
- **24 hours**: `f_TPR=r86400`
- **1 week**: `f_TPR=r604800`

## Time Filter Quick Reference

| Time Period | Seconds | URL Parameter |
|-------------|---------|---------------|
| 1 hour      | 3600    | r3600         |
| 4 hours     | 14400   | r14400        |
| 8 hours     | 28800   | r28800        |
| 24 hours    | 86400   | r86400        |
| 3 days      | 259200  | r259200       |
| 1 week      | 604800  | r604800       |
| 1 month     | 2592000 | r2592000      |

## Pro Tips for Job Hunting

1. **Use Short Time Filters**: Set 1-4 hour filters for frequent checking to catch new postings quickly
2. **Sort by Date**: When using short time filters, sort by "Most Recent" for best results
3. **Location Strategy**: Try both city names and "Remote" for remote positions
4. **Keywords**: Be specific (e.g., "Senior Python Developer" vs "Developer")
5. **Multiple Searches**: Create different URLs for different job types or experience levels

## Examples

### Finding Recent Remote Python Jobs
```bash
python cli.py "Python Developer" --location "Remote" --time "2 hours" --remote remote --sort date_posted
```

### Senior Level Data Science Jobs in Tech Hubs
```bash
python cli.py "Data Scientist" --location "San Francisco" --experience mid_senior,director --time "24 hours" --distance 50
```

### Entry Level Opportunities
```bash
python cli.py "Software Engineer" --experience entry,associate --job-types full_time,internship --time "1 week"
```

## File Structure

```
linkedin_job_searcher/
├── main.py                 # Main application entry point
├── linkedin_url_builder.py # Core URL building logic
├── app.py                  # Streamlit web interface
├── cli.py                  # Command line interface
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Dependencies

- **streamlit**: Web interface framework
- **pyperclip**: Clipboard functionality
- **urllib3**: URL encoding
- **requests**: HTTP functionality
- **validators**: URL validation

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool creates URLs for LinkedIn's public job search. It does not bypass any LinkedIn restrictions or terms of service. Always respect LinkedIn's usage policies and rate limits.

## 🆕 New Features (Latest Update)

### Enhanced Web Interface:
- 🎨 **Improved Button Styling**: Beautiful blue/cyan gradient button with hover effects
- 📋 **Enhanced Copy Functionality**: Reliable clipboard copying with visual feedback
- 🆔 **Job ID Input**: Manual entry field for specific LinkedIn job IDs
- 🌍 **Geographic ID Support**: Optional geo ID input for precise location targeting

### CLI Enhancements:
- `--job-id`: Specify a particular LinkedIn job ID
- `--geo-id`: Use LinkedIn's geographic ID for location precision

### Visual Improvements:
- Modern gradient button styling with smooth animations
- Better error handling and user feedback
- Cleaner interface with improved section headers
