# UUID-generator
An API that generates UUID along with its timestamp whenever the API is called. The most recently generated UUID is displayed along with the already generated UUID(s).

Example of the generated result is given below:

```
{

"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"

"2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",

"2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",

}
```

Only a `get()` method is allowed, and the UUID generated is arranged in the order of the the most recent timestamp.
