"""
This script serves as the entry point for the application. It performs the following actions:
1. Imports the `Configuration` class from `app.configuration.config` and the `Sona` client from `app.client`.
2. Instantiates a `Configuration` object to hold application settings.
3. Creates an instance of the `Sona` application client, passing the configuration object.
4. Runs the application by invoking the `run_app()` method on the `Sona` instance.
Execution begins only if the script is run as the main module.
"""

if __name__ == "__main__":
   
   def main():
      from app import app
      app.run_app()

   main()