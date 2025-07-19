# Project Structure

```
src/
├── device/           # Device-side scripts and configurations
├── python/           # Python source code
│   ├── core/         # Core functionality
│   ├── utils/        # Utility functions
│   └── tests/        # Test files
└── README.md         # This file

data/
├── config/          # Configuration files
└── results/         # Output and result files
```

## Directory Structure

- `src/device/`: Contains scripts and configurations that run on the device side (e.g., a_gdbserver.sh)
- `src/python/`: Main Python source code organized into different modules
  - `core/`: Core functionality of the IoT vulnerability detection framework
  - `utils/`: Helper functions and utilities
  - `tests/`: Test cases for the Python code
- `data/config/`: Configuration files for the project
- `data/results/`: Directory for storing output and result files

## Development Guidelines

1. Keep device-side scripts in `src/device/`
2. Python code should follow the structure in `src/python/`
3. All configurations should be placed in `data/config/`
4. Results and outputs should be stored in `data/results/`
