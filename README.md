# Inventory Tracking system using Django
Screenshots:
![image](https://user-images.githubusercontent.com/20417069/148694150-cf273a7f-4dc3-4645-8c93-e45da8f160f7.png)
![image](https://user-images.githubusercontent.com/20417069/148694171-e7d57db5-e230-487e-a679-218f1cd765b8.png)

Setup:
1. Git Clone the project with: 
  ```
  git clone https://github.com/saiki0007/inventory_tracking.git
  ```
2. Move to the base direcory: 
  ```
  cd inventory_tracking
  ```
3. Make sure you have Python 3.7+
3. Install the dependencies with: 
  ```
  pip install -r requirements.txt
  ```
4. Make migrations with:
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
5. Run the application locally:
  ```
  python3 manage.py runserver
  ```
6. View the application at:
  ```
  http://localhost:8000/inventory_tracker/
