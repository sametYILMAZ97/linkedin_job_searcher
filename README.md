# LinkedIn Job Searcher 🔍

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macOS-lightgrey.svg)

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

### Web Interface (Recommended) 🌐

1. **Start the application**:
   ```bash
   # Option 1: Direct command (Ctrl+C works)
   python run_direct.py

   # Option 2: Using main script
   python main.py --mode web

   # Option 3: Double-click the batch file
   quick_start.bat
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Enter your search criteria**:
   - Keywords/job title
   - Location (use text like "Turkey", "Ankara", or "Remote")
   - Time filter (e.g., "2 hours" for fresh jobs)
   - Work location preferences (checkboxes)

4. **Click the blue "🔗 Generate LinkedIn Search URL" button**
   - URL is automatically generated AND copied to clipboard
   - Success message confirms the copy operation

5. **Paste and search**: Go to LinkedIn and paste the URL, or click the provided link

### Command Line Interface 💻

**Basic job search**:
```bash
python cli.py "Fullstack Developer" --location "Turkey"
```

**Advanced search with time filtering**:
```bash
python cli.py "Data Scientist" --time "2 hours" --location "Remote" --summary
```

**Ultra-fresh job hunting**:
```bash
# Jobs posted in last 30 minutes
python cli.py "Software Engineer" --custom-hours 0.5 --sort date_posted

# Jobs posted in last 4 hours
python cli.py "DevOps Engineer" --time "4 hours" --location "Ankara"
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
| ----------- | ------- | ------------- |
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
├── 📁 .github/
│   ├── copilot-instructions.md    # GitHub Copilot configuration
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD pipeline
├── 📄 .gitignore                  # Git ignore patterns
├── 📄 LICENSE                     # MIT License
├── 📄 README.md                   # This comprehensive guide
├── 📄 requirements.txt            # Python dependencies
├── 🐍 main.py                     # Main application entry point
├── 🐍 linkedin_url_builder.py    # Core URL building logic
├── 🐍 app.py                      # Streamlit web interface
├── 🐍 cli.py                      # Command line interface
├── 🐍 start_app.py               # App starter with background/foreground options
├── 🐍 run_direct.py              # Direct Streamlit runner (Ctrl+C friendly)
├── 📁 Test Files/
│   ├── test_builder.py           # Core functionality tests
│   ├── test_new_features.py      # New features testing
│   ├── test_turkey_geoid.py      # Geographic ID testing
│   └── demo.py                   # Feature demonstration
└── ⚡ quick_start.bat            # Windows batch file for easy startup
```

### 📋 **Key Files Explained:**
- **[`app.py`](app.py)**: Beautiful Streamlit web interface with one-click URL generation
- **[`linkedin_url_builder.py`](linkedin_url_builder.py)**: Core URL manipulation engine
- **[`cli.py`](cli.py)**: Powerful command-line interface for automation
- **[`run_direct.py`](run_direct.py)**: Direct app runner that responds to Ctrl+C properly
- **[`quick_start.bat`](quick_start.bat)**: Easy Windows startup with menu options

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

## 🆕 Latest Features & Updates (v2.0)

### 🎯 **Core Improvements:**
- ✅ **One-Click URL Generation**: Click "Generate" button to automatically copy URL to clipboard
- 🔧 **Fixed Geographic Issues**: Removed unreliable geo ID mappings, now uses text locations
- 📋 **Streamlined UI**: Removed separate copy button for cleaner user experience
- ☑️ **Smart Work Location**: Checkboxes for work arrangements with sensible defaults (On-site + Hybrid selected)

### 🌍 **Geographic Handling:**
- � **Text-Based Locations**: Use city/country names (e.g., "Turkey", "Ankara", "Remote")
- 🔍 **Manual Geo ID Input**: Option to input exact LinkedIn geo IDs when known
- ⚠️ **No Auto-Mapping**: Eliminated problematic automatic geo ID conversions
- 💡 **Clear Instructions**: Step-by-step guide to find correct geo IDs from LinkedIn

### 🎨 **Enhanced User Experience:**
- 🖱️ **One-Click Operation**: Generate and copy URL in single button click
- ✨ **Beautiful Button Styling**: Blue/cyan gradient with smooth hover effects
- 📱 **Responsive Interface**: Clean, modern layout with intuitive controls
- 🔄 **Smart Defaults**: Sensible default selections for quick job searching

### 🚀 **Background Process Management:**
- ⏹️ **Proper App Control**: Multiple ways to start/stop the application
- 🖥️ **Foreground Mode**: Ctrl+C now works properly to stop the app
- 📂 **Batch File Support**: Quick start options via `quick_start.bat`
- 🔧 **VS Code Integration**: Updated tasks for seamless development

### 📊 **Code Quality:**
- ✅ **Formatted Code**: All Python files formatted with Black
- 🔍 **Quality Checks**: Integrated linting and formatting tools
- 🧪 **Comprehensive Testing**: Multiple test files for different scenarios
- 📝 **Better Documentation**: Updated README with current features

## 🌍 **Geographic ID Issues & Solutions**

### **The Problem:**

LinkedIn's geographic IDs change frequently and many online resources have outdated/incorrect mappings. This can cause searches to show jobs from completely different countries!

### **Our Solution:**

1. **Text Location (Recommended)**: Use city/country names like "Turkey", "Ankara", "Remote"
2. **Manual Geo ID**: Find your exact geo ID from LinkedIn and input it manually
3. **No Auto-Mapping**: We removed unreliable auto geo ID mappings

### **How to Find Your Correct Geo ID:**

1. Go to [LinkedIn Jobs](https://www.linkedin.com/jobs/)
2. Search for any job in your desired location
3. Look at the URL after searching
4. Find `geoId=XXXXXX` in the URL
5. Copy that number and use it in the "Manual Geo ID" option

**Example**: If your URL shows:

```
https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=engineer
```

Your geo ID is: `103644278`

## 🔧 Troubleshooting

### **App Won't Stop with Ctrl+C?**
- Use [`run_direct.py`](run_direct.py) instead of [`main.py`](main.py) for proper Ctrl+C support
- Or use: `taskkill /F /IM python.exe` to force stop
- Or run: `python start_app.py --stop`

### **Geographic Issues (Wrong Country Results)?**
- Use text locations like "Turkey", "Ankara" instead of geo IDs
- Find correct geo ID manually from LinkedIn URL after searching
- Enter the geo ID in "Manual Geographic ID" field

### **URL Not Working in LinkedIn?**
- Make sure you're using the full generated URL
- Check that the URL includes `origin=JOB_SEARCH_PAGE_JOB_FILTER`
- Try refreshing the LinkedIn page
- Verify the time filter isn't too restrictive (try 24 hours)

### **Copy to Clipboard Not Working?**
- The app automatically tries to copy when you click "Generate"
- If auto-copy fails, manually select and copy the displayed URL
- Install pyperclip: `pip install pyperclip`

### **No Jobs Found?**
- Try broader keywords
- Increase time filter (e.g., from "1 hour" to "24 hours")
- Check location spelling
- Remove very specific filters to test
