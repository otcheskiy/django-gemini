try:
    import rest_framework
    print("Django REST Framework imported successfully.")
    print(f"Version: {rest_framework.__version__}")
except ImportError as e:
    print(f"Error importing Django REST Framework: {e}")