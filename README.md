# cmpe273-assignment-2

Curl Outputs:
POST for Menu:
curl --header "Content-Type:application/json" \
--request POST \
--data '{
"menu_id": "123",
"store_name": "Pizza Hut",
"selection": [
"Cheese",
"Pepperoni"
],
"size": [
"Slide", "Small", "Medium", "Large", "X-Large"
],
"price": [
"3.50", "7.00", "10.00", "15.00", "20.00"
],
"store_hours": {
"Mon": "10am-10pm",
"Tue": "10am-10pm",
"Wed": "10am-10pm",
"Thu": "10am-10pm",
"Fri": "10am-10pm",
"Sat": "11am-12pm",
"Sun": "11am-12pm"
}
}' \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/menu
Response:
{
"status": 200
}
DELETE for Menu:
curl --header "Content-Type:application/json" \
--request DELETE \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/menu/123
Response:
{
"status": 200
}
PUT for Menu:
curl --header "Content-Type:application/json" \
--request PUT \
--data '{
"selection": ["Cheese","Pepperoni","Vegetable"]
}' \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/menu/123
Response:
{
"status": 200
}
GET for Menu:
curl --header "Content-Type:application/json" \
--request GET \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/menu/123
Response:
{
"menu_id": "123",
"selection": ["Cheese", "Pepperoni", "Vegetable"],
"price": ["3.50", "7.00", "10.00", "15.00", "20.00"],
"store_hours": {
"Wed": "10am-10pm",
"Sun": "11am-12pm",
"Fri": "10am-10pm",
"Tue": "10am-10pm",
"Mon": "10am-10pm",
"Thu": "10am-10pm",
"Sat": "11am-12pm"
},
"store_name": "Pizza Hut",
"size": ["Slide", "Small", "Medium", "Large", "X-Large"]
}
POST for Order:
curl --header "Content-Type:application/json" \
--request POST \
--data '{
"menu_id": "123",
"order_id": "1234",
"customer_name": "John Smith",
"customer_email": "foobar@gmail.com"
}' \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/order
Response:
{
"status": 200,
"Message": "Hi John Smith, please choose one of these
selection: 1. Cheese, 2. Pepperoni, 3. Vegetable"
}
PUT for Order:
curl --header "Content-Type:application/json" \
--request PUT \
--data '{
"input": "1"
}' \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/order/1234
Response:
{
"status": 200,
"Message": "Which size do you want?: 1. Slide, 2. Small, 3.
Medium, 4. Large, 5. X-Large"
}
PUT for Order:
curl --header "Content-Type:application/json" \
--request PUT \
--data '{
"input": "1"
}' \
https://3qq6hnwmif.execute-api.us-west-
2.amazonaws.com/myApp/order/1234
Response:
{
"status": 200,
"Message": "Your order costs 15.00. We will email you when the
order is ready. Thank you!"
}
GET for Order:
curl --header "Content-Type:application/json" \
--request GET \
https://3qq6hnwmif.execute-api.us-west-2.amazonaws.com/myApp/order/1234
Response:
{
"status": 200,
"menu_id": "123",
"customer_email": "foobar@gmail.com",
"order_id": "1234",
"order_status": "processing",
"order": {
"selection": "Pepperoni",
"costs": "20.00",
"order_time": "20.00",
"size": "X-Large"
},
"customer_name": "John Smith"
}
