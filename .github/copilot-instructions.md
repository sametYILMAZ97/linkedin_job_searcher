<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# LinkedIn Job Searcher - Copilot Instructions

This is a Python-based LinkedIn job search URL builder tool with the following characteristics:

## Project Overview
- **Purpose**: Generate optimized LinkedIn job search URLs with advanced filtering
- **Main Components**: URL builder class, Streamlit web UI, CLI interface
- **Target Users**: Job seekers who want to create precise LinkedIn searches

## Code Style & Patterns
- Use Python type hints for all function parameters and return values
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Include comprehensive docstrings for all classes and methods
- Prefer composition over inheritance
- Use builder pattern for URL construction

## Key Technologies
- **Python 3.8+**: Core language
- **Streamlit**: Web interface framework
- **urllib.parse**: URL encoding and manipulation
- **argparse**: Command-line interface
- **pyperclip**: Clipboard functionality

## LinkedIn URL Parameters
When working with LinkedIn URLs, remember these key parameters:
- `f_TPR=r{seconds}`: Time filter (r3600 = 1 hour, r86400 = 24 hours)
- `keywords`: Job search terms
- `location`: Geographic location
- `distance`: Search radius in miles
- `sortBy`: R (relevance) or DD (date posted)
- `f_E`: Experience level codes (1-6)
- `f_JT`: Job type codes (F, P, C, T, I, V, O)
- `f_WT`: Work arrangement (1=on-site, 2=remote, 3=hybrid)

## Development Guidelines
1. **URL Building**: Always URL-encode parameters properly
2. **Error Handling**: Provide graceful fallbacks for invalid inputs
3. **User Experience**: Give clear feedback and helpful error messages
4. **Validation**: Validate user inputs before processing
5. **Documentation**: Include examples in docstrings

## Testing Considerations
- Test URL generation with various parameter combinations
- Verify proper URL encoding of special characters
- Test time filter conversions (hours to seconds)
- Validate parameter mapping for experience levels, job types, etc.
- Test both web and CLI interfaces

## Common Tasks
- Adding new filter parameters to LinkedIn URLs
- Improving the Streamlit UI layout and user experience
- Extending CLI functionality with new options
- Adding validation for LinkedIn-specific constraints
- Optimizing URL generation performance

## Code Examples
When adding new features, follow these patterns:

```python
# URL Builder Method Pattern
def set_new_filter(self, value: str) -> 'LinkedInURLBuilder':
    """Set a new filter parameter."""
    if value and self._validate_input(value):
        self.params['new_param'] = self._encode_value(value)
    return self

# Streamlit Component Pattern
st.subheader("New Filter")
new_value = st.selectbox(
    "Select option",
    options=['option1', 'option2'],
    help="Helpful description of what this filter does"
)
```

Focus on maintainability, user experience, and accurate LinkedIn URL generation.
