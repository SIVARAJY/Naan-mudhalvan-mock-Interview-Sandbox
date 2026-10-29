import os
import json
import re
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# --- RAW MCQ DATA PROVIDED BY USER ---
raw_text = """
Part 1: HTML (1–15)
1. What does HTML stand for?
A) Hyper Text Markup Language B) High Text Machine Language C) Hyper Transfer Markup Language D) Home Tool Markup Language
Answer: A) Hyper Text Markup Language
2. Which tag is used to create a hyperlink in HTML?
A) <link> B) <a> C) <href> D) <url>
Answer: B) <a>
3. Which HTML tag is used to display an image?
A) <picture> B) <image> C) <img> D) <src>
Answer: C) <img>
4. Which tag creates the largest heading by default?
A) <h6> B) <head> C) <heading> D) <h1>
Answer: D) <h1>
5. Which attribute specifies an image's location?
A) href B) src C) alt D) link
Answer: B) src
6. Which tag is used to create an unordered list?
A) <ol> B) <li> C) <ul> D) <list>
Answer: C) <ul>
7. Which tag defines a paragraph?
A) <p> B) <para> C) <text> D) <pg>
Answer: A) <p>
8. Which attribute provides alternative text for an image?
A) title B) src C) alt D) name
Answer: C) alt
9. Which HTML tag creates a table row?
A) <td> B) <th> C) <table-row> D) <tr>
Answer: D) <tr>
10. Which input type hides the entered characters?
A) text B) password C) hidden-text D) secure
Answer: B) password
11. Which tag inserts a line break?
A) <break> B) <lb> C) <br> D) <hr>
Answer: C) <br>
12. Which HTML tag is used to create a form?
A) <form> B) <input> C) <fieldset> D) <submit>
Answer: A) <form>
13. Which attribute makes a form field mandatory?
A) validate B) required C) mandatory D) must
Answer: B) required
14. Which semantic HTML element represents the main content of a page?
A) <footer> B) <aside> C) <main> D) <nav>
Answer: C) <main>
15. Which declaration specifies an HTML5 document?
A) <html5> B) <!DOCTYPE html> C) <doctype html5> D) <!HTML>
Answer: B) <!DOCTYPE html>
Part 2: CSS (16–30)
16. What does CSS stand for?
A) Computer Style Sheets B) Creative Style System C) Cascading Style Sheets D) Colorful Style Sheets
Answer: C) Cascading Style Sheets
17. Which property changes the text color?
A) font-color B) color C) text-color D) foreground
Answer: B) color
18. Which CSS property changes the background color?
A) background-color B) color-background C) bgcolor D) background-style
Answer: A) background-color
19. Which symbol selects an element by its ID in CSS?
A) . B) * C) # D) @
Answer: C) #
20. Which symbol selects elements by class?
A) # B) . C) $ D) &
Answer: B) .
21. Which property controls text size?
A) font-style B) text-height C) font-size D) text-size
Answer: C) font-size
22. Which CSS property makes text bold?
A) font-weight B) text-bold C) font-style D) text-weight
Answer: A) font-weight
23. Which property adds space inside an element's border?
A) margin B) padding C) outline D) spacing
Answer: B) padding
24. Which property adds space outside an element's border?
A) padding B) border-spacing C) margin D) gap
Answer: C) margin
25. Which CSS layout system is designed primarily for one-dimensional layouts?
A) Flexbox B) CSS Grid C) Float D) Positioning
Answer: A) Flexbox
26. Which CSS system is especially useful for two-dimensional layouts?
A) Flexbox B) CSS Grid C) Inline layout D) Float
Answer: B) CSS Grid
27. Which property rounds an element's corners?
A) corner-style B) border-radius C) border-round D) radius-style
Answer: B) border-radius
28. Which CSS rule is commonly used for responsive design at different screen widths?
A) @font-face B) @keyframes C) @media D) @import-only
Answer: C) @media
29. Which property controls the stacking order of positioned elements?
A) position-index B) layer C) z-index D) stack-order
Answer: C) z-index
30. Which CSS unit is relative to the root element's font size?
A) px B) rem C) cm D) pt
Answer: B) rem
Part 3: JavaScript (31–50)
31. What is JavaScript mainly used for in web development?
A) Styling web pages B) Making web pages interactive C) Storing files only D) Creating database tables only
Answer: B) Making web pages interactive
32. Which keyword declares a block-scoped variable that can be reassigned?
A) const B) fixed C) let D) static
Answer: C) let
33. Which keyword declares a variable that cannot be reassigned?
A) const B) var C) let D) change
Answer: A) const
34. Which operator checks both value and type equality?
A) = B) == C) === D) !=
Answer: C) ===
35. Which function displays a message in the browser's console?
A) print() B) console.log() C) display() D) echo()
Answer: B) console.log()
36. Which symbol is used for single-line comments in JavaScript?
A) <!-- --> B) ## C) // D) **
Answer: C) //
37. Which method selects an element by its ID?
A) document.getElementById() B) document.getClass() C) document.selectId() D) document.find()
Answer: A) document.getElementById()
38. Which method adds an event listener to an element?
A) addEvent() B) attach() C) addEventListener() D) listenEvent()
Answer: C) addEventListener()
39. Which event occurs when a user clicks an element?
A) change B) click C) hover D) load
Answer: B) click
40. Which JavaScript data type represents a true or false value?
A) String B) Number C) Boolean D) Object
Answer: C) Boolean
41. Which array method adds an element to the end of an array?
A) pop() B) push() C) shift() D) remove()
Answer: B) push()
42. Which array method removes the last element?
A) push() B) shift() C) pop() D) slice()
Answer: C) pop()
43. Which keyword defines a function in JavaScript?
A) function B) method C) define D) func
Answer: A) function
44. What does DOM stand for?
A) Data Object Model B) Document Object Model C) Digital Ordinance Model D) Document Oriented Method
Answer: B) Document Object Model
45. Which operator is used for logical AND?
A) || B) ! C) && D) &=
Answer: C) &&
46. Which statement handles errors using a catch block?
A) if-else B) try-catch C) for-loop D) switch-case
Answer: B) try-catch
47. What does JSON stand for?
A) Java Standard Object Notation B) JavaScript Object Notation C) Java Source Open Network D) JavaScript Online Network
Answer: B) JavaScript Object Notation
48. Which method converts a JSON string into a JavaScript object?
A) JSON.stringify() B) JSON.parse() C) JSON.convert() D) JSON.object()
Answer: B) JSON.parse()
49. Which JavaScript feature is commonly used to handle asynchronous operations?
A) Promises B) CSS selectors C) HTML attributes D) Table rows
Answer: A) Promises
50. Which keyword is commonly used to wait for a Promise inside an async function?
A) wait B) pause C) await D) delay
Answer: C) await
Part 4: Frontend Development (51–60)
51. What is frontend development?
A) Developing the user-facing part of a website B) Managing hardware components C) Installing operating systems D) Designing database servers only
Answer: A) Developing the user-facing part of a website
52. Which of the following is a frontend JavaScript library?
A) MySQL B) React C) Node.js D) MongoDB
Answer: B) React
53. What is the main purpose of React components?
A) Store passwords B) Build reusable UI parts C) Configure network cables D) Replace the database
Answer: B) Build reusable UI parts
54. What is JSX in React?
A) A database language B) A CSS framework C) A syntax extension that lets you write HTML-like markup in JavaScript D) A web server
Answer: C) A syntax extension that lets you write HTML-like markup in JavaScript
55. Which React hook is used to manage local component state?
A) useState B) useRoute C) useStyle D) useHTML
Answer: A) useState
56. Which React hook is commonly used for side effects?
A) useCSS B) useEffect C) usePage D) useClass
Answer: B) useEffect
57. What is responsive web design?
A) A website that works only on desktops B) A website that adapts to different screen sizes C) A website without CSS D) A website that requires a separate page for every device
Answer: B) A website that adapts to different screen sizes
58. Which HTML attribute helps make a page responsive on mobile devices?
A) charset B) alt C) viewport through the name attribute of a meta tag D) target
Answer: C) viewport through the name attribute of a meta tag
59. Which tool helps developers inspect HTML, CSS, and JavaScript in a browser?
A) Browser Developer Tools B) Calculator C) File Explorer only D) Paint
Answer: A) Browser Developer Tools
60. What is the primary purpose of a CSS framework such as Bootstrap?
A) Manage database records B) Speed up interface development using reusable styles and components C) Host websites D) Execute SQL queries
Answer: B) Speed up interface development using reusable styles and components
Part 5: Backend Development (61–70)
61. What is backend development?
A) Designing only page colors B) Building server-side logic and data handling C) Writing image captions D) Creating website logos only
Answer: B) Building server-side logic and data handling
62. Which of the following is a JavaScript runtime used for backend development?
A) HTML B) CSS C) Node.js D) Bootstrap
Answer: C) Node.js
63. Which framework is commonly used with Node.js to build web servers?
A) Express.js B) Bootstrap C) React D) Tailwind CSS
Answer: A) Express.js
64. What is the primary role of a web server?
A) Draw pictures B) Receive requests and return responses C) Design CSS styles D) Edit documents
Answer: B) Receive requests and return responses
65. What does API stand for?
A) Application Programming Interface B) Advanced Program Installation C) Automated Page Internet D) Application Process Integration
Answer: A) Application Programming Interface
66. Which HTTP method is commonly used to retrieve data?
A) POST B) GET C) DELETE D) PATCH
Answer: B) GET
67. Which HTTP method is commonly used to submit data to create a resource?
A) GET B) TRACE C) POST D) OPTIONS
Answer: C) POST
68. What is middleware in a web framework?
A) A function that processes requests and responses during the request-response cycle B) A type of monitor C) A database table D) A CSS property
Answer: A) A function that processes requests and responses during the request-response cycle
69. What is authentication?
A) Determining what a user is allowed to do B) Verifying a user's identity C) Compressing website images D) Formatting a web page
Answer: B) Verifying a user's identity
70. What is authorization?
A) Checking a user's permissions to access a resource B) Creating a new username C) Styling a login page D) Registering a domain name
Answer: A) Checking a user's permissions to access a resource
Part 6: Databases and APIs (71–80)
71. What is the primary purpose of a database in a web application?
A) Style web pages B) Store and manage data C) Render animations D) Compile CSS
Answer: B) Store and manage data
72. Which of the following is a relational database management system?
A) React B) Express.js C) MySQL D) HTML
Answer: C) MySQL
73. Which of the following is a NoSQL database?
A) MongoDB B) CSS C) JavaScript D) Bootstrap
Answer: A) MongoDB
74. What does SQL stand for?
A) Structured Query Language B) Simple Question List C) System Quality Logic D) Standard Quick Link
Answer: A) Structured Query Language
75. Which SQL command retrieves records from a table?
A) UPDATE B) SELECT C) DELETE D) CREATE
Answer: B) SELECT
76. What is a primary key?
A) A column that uniquely identifies each record in a table B) A password for a database server C) A duplicate row D) A CSS class
Answer: A) A column that uniquely identifies each record in a table
77. What is the purpose of a foreign key?
A) To change a web page's font B) To link records between related tables C) To encrypt every database field automatically D) To create HTML forms
Answer: B) To link records between related tables
78. What is a REST API?
A) An API designed around resource-oriented interactions and HTTP conventions B) A CSS layout system C) A programming language D) An image format
Answer: A) An API designed around resource-oriented interactions and HTTP conventions
79. What is an API endpoint?
A) A database password B) A specific URL or address where an API resource or operation can be accessed C) A CSS selector D) A browser extension
Answer: B) A specific URL or address where an API resource or operation can be accessed
80. Which HTTP status code commonly indicates a successful request?
A) 404 B) 500 C) 200 D) 403
Answer: C) 200
Part 7: HTTP and Web Hosting (81–90)
81. What does HTTP stand for?
A) Hypertext Transfer Protocol B) High Transfer Text Program C) Hyper Tool Transmission Process D) Home Text Transfer Protocol
Answer: A) Hypertext Transfer Protocol
82. What is the main difference between HTTP and HTTPS?
A) HTTPS uses TLS to secure communication B) HTTP is used only for images C) HTTPS cannot transfer data D) HTTP always requires a password
Answer: A) HTTPS uses TLS to secure communication
83. What does the HTTP status code 404 mean?
A) Request successful B) Resource not found C) Server error D) Access granted
Answer: B) Resource not found
84. What does HTTP status code 500 indicate?
A) Internal server error B) Page permanently moved C) Request successful D) Resource not found
Answer: A) Internal server error
85. What is a domain name?
A) A human-readable address used to access a website B) A database table C) A JavaScript function D) A CSS property
Answer: A) A human-readable address used to access a website
86. What is web hosting?
A) Creating website colors B) Providing server resources to make a website accessible online C) Writing HTML comments D) Designing a database query
Answer: B) Providing server resources to make a website accessible online
87. What does DNS do?
A) Converts domain names into corresponding IP addresses and other DNS records B) Creates HTML files C) Encrypts all passwords D) Formats CSS files
Answer: A) Converts domain names into corresponding IP addresses and other DNS records
88. What is a cookie in web development?
A) A small piece of data stored by the browser for a website B) A database server C) An image editor D) A programming framework
Answer: A) A small piece of data stored by the browser for a website
89. What is a session commonly used for?
A) Maintaining user-related state across multiple requests B) Changing font size C) Compressing images D) Creating domain names
Answer: A) Maintaining user-related state across multiple requests
90. What is a CDN?
A) Content Delivery Network B) Computer Data Number C) Central Design Node D) Code Development Name
Answer: A) Content Delivery Network
Part 8: Web Security and Best Practices (91–100)
91. What does XSS stand for?
A) Extra Secure System B) Cross-Site Scripting C) External Server Storage D) Cross-System Software
Answer: B) Cross-Site Scripting
92. What is SQL injection?
A) A database backup method B) An attack that manipulates SQL queries through untrusted input C) A CSS technique D) A type of web hosting
Answer: B) An attack that manipulates SQL queries through untrusted input
93. Which is a recommended way to store user passwords?
A) Store them as plain text B) Store them in a public file C) Hash them with a suitable password-hashing algorithm and a unique salt D) Store them in the page's HTML
Answer: C) Hash them with a suitable password-hashing algorithm and a unique salt
94. What is the purpose of input validation?
A) Ensure input meets expected rules before processing it B) Change website colors C) Increase image size D) Automatically create accounts
Answer: A) Ensure input meets expected rules before processing it
95. What is Git commonly used for?
A) Version control B) Database hosting C) CSS styling D) Image compression only
Answer: A) Version control
96. Which Git command creates a local copy of an existing repository?
A) git push B) git clone C) git delete D) git style
Answer: B) git clone
97. What is the purpose of testing a web application?
A) Identify bugs and verify expected behavior B) Remove all HTML C) Replace the backend D) Increase the number of pages
Answer: A) Identify bugs and verify expected behavior
98. What does accessibility in web development mean?
A) Making websites usable by people with different abilities B) Allowing only developers to use a website C) Making every page private D) Removing all images
Answer: A) Making websites usable by people with different abilities
99. What is lazy loading?
A) Loading resources only when they are needed or approaching use B) Preventing a website from opening C) Loading all resources twice D) Disabling JavaScript
Answer: A) Loading resources only when they are needed or approaching use
100. Which practice generally improves website performance?
A) Using unnecessarily large images B) Loading every script synchronously C) Optimizing images and reducing unnecessary code D) Duplicating all resources
Answer: C) Optimizing images and reducing unnecessary code

Part 1: Java Basics (1–10)
1. Who developed Java?
A) Dennis Ritchie B) James Gosling C) Guido van Rossum D) Bjarne Stroustrup
Answer: B) James Gosling
2. Which company originally developed Java?
A) Microsoft B) Apple C) Sun Microsystems D) IBM
Answer: C) Sun Microsystems
3. Which extension is used for Java source files?
A) .py B) .class C) .java D) .js
Answer: C) .java
4. Which method is the usual entry point of a standalone Java application?
A) start() B) main() C) run() D) init()
Answer: B) main()
5. Which keyword is used to define a class in Java?
A) define B) struct C) class D) object
Answer: C) class
6. What does JVM stand for?
A) Java Variable Method B) Java Virtual Machine C) Java Verified Mode D) Java Visual Model
Answer: B) Java Virtual Machine
7. What does JDK stand for?
A) Java Development Kit B) Java Design Keyword C) Java Deployment Kernel D) Java Data Kit
Answer: A) Java Development Kit
8. What does JRE stand for?
A) Java Runtime Environment B) Java Reading Engine C) Java Remote Execution D) Java Resource Editor
Answer: A) Java Runtime Environment
9. Which command compiles a Java source file?
A) java B) javac C) compile D) jvm
Answer: B) javac
10. Which command is commonly used to run a compiled Java class?
A) javac B) java C) runjava D) execute
Answer: B) java
Part 2: Data Types and Variables (11–20)
11. Which of the following is a primitive data type in Java?
A) String B) Array C) int D) Scanner
Answer: C) int
12. Which data type stores a single 16-bit Unicode character?
A) char B) String C) boolean D) byte
Answer: A) char
13. Which data type stores true or false values?
A) int B) boolean C) char D) double
Answer: B) boolean
14. Which data type is commonly used to store decimal values with double precision?
A) int B) boolean C) double D) char
Answer: C) double
15. What is the size of an int in Java?
A) 8 bits B) 16 bits C) 32 bits D) 64 bits
Answer: C) 32 bits
16. Which keyword declares a variable whose value cannot be reassigned after initialization?
A) static B) final C) constant D) fixed
Answer: B) final
17. Which of the following is a valid Java variable name?
A) 2value B) my-value C) myValue D) class
Answer: C) myValue
18. What is the default value of an instance variable of type int?
A) 1 B) -1 C) 0 D) null
Answer: C) 0
19. Which data type can store the largest range of integer values among these options?
A) byte B) short C) int D) long
Answer: D) long
20. Which keyword is used to create an object in Java?
A) class B) new C) this D) object
Answer: B) new
Part 3: Operators (21–30)
21. Which operator is used for addition?
A) * B) + C) % D) //
Answer: B) +
22. What is the output of System.out.println(10 / 3);?
A) 3.33 B) 3 C) 4 D) 1
Answer: B) 3
23. What is the output of System.out.println(10 % 3);?
A) 3 B) 0 C) 1 D) 10
Answer: C) 1
24. Which operator checks equality between primitive values?
A) = B) == C) != D) :=
Answer: B) ==
25. Which operator means logical AND?
A) || B) ! C) && D) &=
Answer: C) &&
26. What is the output of System.out.println(5 > 3);?
A) 5 B) 3 C) true D) false
Answer: C) true
27. Which operator increments a variable by one?
A) -- B) ++ C) ** D) //
Answer: B) ++
28. What is the output of System.out.println(2 + 3 * 4);?
A) 20 B) 14 C) 24 D) 11
Answer: B) 14
29. Which operator represents logical OR?
A) && B) ! C) || D) ==
Answer: C) ||
30. What is the output of System.out.println(5 != 5);?
A) true B) false C) 5 D) Error
Answer: B) false
Part 4: Conditional Statements and Loops (31–40)
31. Which statement executes code when a condition is true?
A) if B) import C) class D) package
Answer: A) if
32. Which keyword provides an alternative condition after if?
A) otherwise B) elseif C) else if D) then
Answer: C) else if
33. Which loop is commonly used when the number of iterations is known?
A) for B) switch C) if D) try
Answer: A) for
34. Which loop checks its condition before each iteration?
A) do-while only B) while C) Neither while nor for D) switch
Answer: B) while
35. Which loop executes its body at least once?
A) for B) while C) do-while D) Enhanced for only
Answer: C) do-while
36. Which keyword terminates the nearest enclosing loop?
A) skip B) stop C) break D) exitloop
Answer: C) break
37. Which keyword skips the current iteration of a loop?
A) break B) continue C) return D) pass
Answer: B) continue
38. Which statement is commonly used to select among multiple cases based on one expression?
A) switch B) while C) try D) extends
Answer: A) switch
39. What is the output of the following code?
for (int i = 0; i < 3; i++) {
    System.out.print(i);
}
A) 123 B) 012 C) 0123 D) 321
Answer: B) 012
40. How many times does while (false) execute its body?
A) Once B) Twice C) Zero times D) Infinitely
Answer: C) Zero times
Part 5: Arrays and Strings (41–50)
41. Which syntax correctly declares an integer array?
A) int arr; B) int[] arr; C) array int arr; D) arr int[];
Answer: B) int[] arr;
42. What is the index of the first element in a Java array?
A) 0 B) 1 C) -1 D) 2
Answer: A) 0
43. Which property returns the length of an array?
A) size() B) length() C) length D) count()
Answer: C) length
44. What is the output of the following code?
int[] a = {10, 20, 30};
System.out.println(a[1]);
A) 10 B) 20 C) 30 D) 1
Answer: B) 20
45. Which class represents strings in Java?
A) Text B) String C) CharArray D) Sentence
Answer: B) String
46. Are Java String objects mutable?
A) Yes B) No C) Only numbers in strings are mutable D) Only empty strings are mutable
Answer: B) No
47. Which method returns the number of characters in a string?
A) size() B) length() C) count() D) capacity()
Answer: B) length()
48. Which method compares the contents of two strings?
A) == B) compare() C) equals() D) same()
Answer: C) equals()
49. What is the output of "Java".charAt(0)?
A) J B) a C) v D) Java
Answer: A) J
50. Which class is suitable for building a mutable string efficiently?
A) String B) StringBuilder C) Integer D) Character
Answer: B) StringBuilder
Part 6: Object-Oriented Programming (51–60)
51. What does OOP stand for?
A) Object-Oriented Programming B) Online Operating Program C) Object Output Processing D) Ordered Operation Protocol
Answer: A) Object-Oriented Programming
52. Which keyword defines a class in Java?
A) object B) class C) define D) struct
Answer: B) class
53. What is an object?
A) An instance of a class B) A loop C) A package only D) A data type keyword
Answer: A) An instance of a class
54. Which method has the same name as its class and no return type?
A) Main method B) Constructor C) Static method D) Abstract method
Answer: B) Constructor
55. Which keyword refers to the current object?
A) super B) this C) self D) current
Answer: B) this
56. Which keyword is used for class inheritance?
A) implements B) inherits C) extends D) superclass
Answer: C) extends
57. Which keyword is used when a class implements an interface?
A) extends B) implements C) interface D) inherits
Answer: B) implements
58. Which OOP concept hides internal implementation details and exposes a controlled interface?
A) Encapsulation B) Iteration C) Compilation D) Recursion
Answer: A) Encapsulation
59. What is method overloading?
A) Defining methods with the same name but different parameter lists B) Defining methods only in different classes C) Deleting a method D) Calling a method repeatedly
Answer: A) Defining methods with the same name but different parameter lists
60. What is method overriding?
A) A subclass providing its own implementation of an inherited method B) Declaring two variables with the same name in one scope C) Creating multiple constructors only D) Calling a static method
Answer: A) A subclass providing its own implementation of an inherited method
Part 7: Inheritance, Interfaces and Access Modifiers (61–70)
61. Which access modifier makes a member accessible from anywhere, subject to module and other language-access rules?
A) private B) protected C) public D) Default access
Answer: C) public
62. Which access modifier restricts direct access to the declaring class?
A) public B) private C) protected D) static
Answer: B) private
63. Which keyword prevents a class from being subclassed?
A) static B) final C) private D) void
Answer: B) final
64. Which keyword refers to the superclass's members or constructor?
A) this B) parent C) super D) base
Answer: C) super
65. Can a Java class directly extend more than one class?
A) Yes, any number B) Yes, exactly two C) No D) Only if both classes are abstract
Answer: C) No
66. Can a Java class implement multiple interfaces?
A) Yes B) No C) Only one D) Only if it is abstract
Answer: A) Yes
67. Which keyword declares an interface?
A) implements B) interface C) extends D) abstract
Answer: B) interface
68. Which keyword declares an abstract class?
A) abstract B) virtual C) interface D) static
Answer: A) abstract
69. What is polymorphism in OOP?
A) One interface or reference supporting different implementations or behaviors B) Restricting all methods to private C) Storing only integers D) Preventing inheritance
Answer: A) One interface or reference supporting different implementations or behaviors
70. What is encapsulation commonly achieved through?
A) Combining data and methods in a class and controlling access B) Using loops only C) Deleting constructors D) Avoiding all objects
Answer: A) Combining data and methods in a class and controlling access
Part 8: Exception Handling (71–80)
71. Which keyword begins an exception-handling block?
A) catch B) try C) throw D) error
Answer: B) try
72. Which block handles an exception?
A) catch B) final C) throws D) break
Answer: A) catch
73. Which block is generally used for cleanup code?
A) try B) catch C) finally D) throw
Answer: C) finally
74. Which keyword explicitly throws an exception?
A) throws B) throw C) catch D) error
Answer: B) throw
75. Which keyword declares exceptions a method may pass to its caller?
A) throw B) throws C) catch D) final
Answer: B) throws
76. Which exception is commonly raised when an integer is divided by zero?
A) IOException B) ArithmeticException C) NullPointerException D) ClassNotFoundException
Answer: B) ArithmeticException
77. Which exception can occur when accessing a method or field through a null reference?
A) ArithmeticException B) NullPointerException C) IOException D) NumberFormatException
Answer: B) NullPointerException
78. Which of the following is a checked exception?
A) NullPointerException B) ArithmeticException C) IOException D) ArrayIndexOutOfBoundsException
Answer: C) IOException
79. Which superclass is the root of Java's exception and error hierarchy?
A) Object B) Exception C) Throwable D) RuntimeException
Answer: C) Throwable
80. Which block can be used to handle multiple different exception types?
A) Multiple catch blocks B) Multiple main methods only C) Multiple constructors only D) Multiple packages
Answer: A) Multiple catch blocks
Part 9: Collections Framework (81–90)
81. Which interface represents an ordered collection that can contain duplicates?
A) List B) Set C) Map D) Queue only
Answer: A) List
82. Which collection does not permit duplicate elements?
A) ArrayList B) LinkedList C) HashSet D) Vector
Answer: C) HashSet
83. Which collection stores key-value pairs?
A) List B) Map C) Set D) Iterator
Answer: B) Map
84. Which class provides a resizable array implementation of List?
A) HashMap B) ArrayList C) HashSet D) TreeMap
Answer: B) ArrayList
85. Which class implements a doubly linked list and the List interface?
A) ArrayList B) LinkedList C) HashMap D) TreeSet
Answer: B) LinkedList
86. Which collection stores elements in sorted order according to their natural ordering or a comparator?
A) HashSet B) TreeSet C) ArrayList D) Stack
Answer: B) TreeSet
87. Which interface is commonly used to traverse elements in a collection?
A) Iterator B) Scanner C) Runnable D) Comparable only
Answer: A) Iterator
88. Which method adds an element to an ArrayList?
A) insertItem() B) append() C) add() D) pushItem()
Answer: C) add()
89. Which class commonly implements a hash-table-based map?
A) HashMap B) ArrayList C) TreeSet D) LinkedList
Answer: A) HashMap
90. Which interface represents a collection designed for holding elements before processing, often in FIFO order?
A) Queue B) Map C) Set D) Comparable
Answer: A) Queue
Part 10: Multithreading and Miscellaneous (91–100)
91. What is a thread?
A) A lightweight unit of execution within a process B) A database table C) A Java package only D) A variable type
Answer: A) A lightweight unit of execution within a process
92. Which method contains the code executed by a typical Java thread?
A) start() B) run() C) mainThread() D) executeNow()
Answer: B) run()
93. Which method starts a new thread of execution when called on a Thread instance?
A) run() B) start() C) init() D) begin()
Answer: B) start()
94. Which keyword helps control access to a critical section for an object monitor?
A) volatile B) synchronized C) transient D) native
Answer: B) synchronized
95. Which interface is commonly implemented to define a task for a thread?
A) Serializable B) Runnable C) Comparable D) Cloneable
Answer: B) Runnable
96. Which package contains many fundamental Java classes, including String and System?
A) java.io B) java.util C) java.lang D) java.net
Answer: C) java.lang
97. Which class can read user input from the keyboard?
A) Scanner B) StringBuilder C) Thread D) FileWriter
Answer: A) Scanner
98. Which statement correctly prints text followed by a newline?
A) System.print("Hello"); B) System.out.println("Hello"); C) Console.display("Hello"); D) print.System("Hello");
Answer: B) System.out.println("Hello");
99. What is the output of the following code?
int x = 5;
System.out.println(x++);
A) 4 B) 5 C) 6 D) Error
Answer: B) 5
100. What is the output of the following code?
String s = "Java";
System.out.println(s.length());
A) 3 B) 4 C) 5 D) Error
Answer: B) 4

Part 1: DBMS Basics (1–10)
1. What is the full form of DBMS?
A) Data Backup Management System B) Database Management System C) Digital Base Management Software D) Database Monitoring Service
Answer: B) Database Management System
2. What is the main purpose of a DBMS?
A) To create animations B) To manage and organize data C) To design websites only D) To compile programs
Answer: B) To manage and organize data
3. Which of the following is an example of a DBMS?
A) MySQL B) HTML C) CSS D) JavaScript
Answer: A) MySQL
4. What is a database?
A) A collection of organized data B) A programming language C) An operating system D) A computer network
Answer: A) A collection of organized data
5. Which of the following is a relational DBMS?
A) MySQL B) MS Paint C) Notepad D) PowerPoint
Answer: A) MySQL
6. What does RDBMS stand for?
A) Remote Database Management System B) Relational Database Management System C) Rapid Data Backup Management System D) Random Database Monitoring System
Answer: B) Relational Database Management System
7. In a relational database, data is mainly organized into:
A) Tables B) Images C) Slides D) Programs
Answer: A) Tables
8. What is a row in a database table called?
A) Attribute B) Record C) Column D) Schema
Answer: B) Record
9. What is a column in a database table called?
A) Tuple B) Record C) Attribute D) Database
Answer: C) Attribute
10. Which language is commonly used to interact with relational databases?
A) SQL B) HTML C) CSS D) XML
Answer: A) SQL
Part 2: SQL Basics (11–20)
11. What does SQL stand for?
A) Structured Query Language B) Simple Question Language C) Standard Queue Language D) System Query Logic
Answer: A) Structured Query Language
12. Which SQL command retrieves data from a table?
A) INSERT B) SELECT C) UPDATE D) DELETE
Answer: B) SELECT
13. Which command inserts new records into a table?
A) ADD B) INSERT C) CREATE D) ALTER
Answer: B) INSERT
14. Which command modifies existing records?
A) UPDATE B) SELECT C) DROP D) CREATE
Answer: A) UPDATE
15. Which command removes selected records from a table?
A) REMOVE B) DROP C) DELETE D) CLEAR
Answer: C) DELETE
16. Which SQL clause filters rows based on a condition?
A) ORDER BY B) WHERE C) GROUP BY D) SELECT
Answer: B) WHERE
17. Which clause sorts query results?
A) SORT B) ORDER BY C) GROUP BY D) ARRANGE
Answer: B) ORDER BY
18. Which keyword removes duplicate rows from query results?
A) UNIQUE B) DISTINCT C) DIFFERENT D) REMOVE
Answer: B) DISTINCT
19. Which function counts the number of rows?
A) SUM() B) AVG() C) COUNT() D) TOTAL()
Answer: C) COUNT()
20. Which SQL clause groups rows with matching values?
A) GROUP BY B) ORDER BY C) WHERE D) DISTINCT
Answer: A) GROUP BY
Part 3: Keys in DBMS (21–30)
21. What is a primary key?
A) A key that uniquely identifies each row B) A key that allows duplicate values C) A key used only for sorting D) A key that stores passwords only
Answer: A) A key that uniquely identifies each row
22. Can a primary key contain NULL values?
A) Yes, always B) No C) Only one NULL value D) Only in large tables
Answer: B) No
23. What is a foreign key used for?
A) To connect related tables B) To delete an entire database C) To sort rows D) To encrypt all data
Answer: A) To connect related tables
24. Which key can contain more than one attribute to uniquely identify a row?
A) Composite key B) Foreign key only C) Duplicate key D) Null key
Answer: A) Composite key
25. What is a candidate key?
A) An attribute or set of attributes that can uniquely identify a row B) A key that always contains NULL C) A key used only for sorting D) A key that permits duplicate identifiers
Answer: A) An attribute or set of attributes that can uniquely identify a row
26. What is a super key?
A) Any set of attributes that uniquely identifies a row B) A key that cannot identify rows C) A key that always contains two columns D) A key used only in sorting
Answer: A) Any set of attributes that uniquely identifies a row
27. What is an alternate key?
A) A candidate key not selected as the primary key B) A foreign key with NULL values C) A duplicate key D) A key used only for encryption
Answer: A) A candidate key not selected as the primary key
28. Which constraint ensures that values in a column are unique?
A) CHECK B) UNIQUE C) DEFAULT D) NOT NULL
Answer: B) UNIQUE
29. Which key establishes a relationship with a key in another table?
A) Primary key B) Foreign key C) Alternate key D) Super key only
Answer: B) Foreign key
30. Which constraint prevents a column from storing NULL values?
A) UNIQUE B) DEFAULT C) NOT NULL D) CHECK
Answer: C) NOT NULL
Part 4: SQL Commands and Constraints (31–40)
31. Which SQL command creates a new table?
A) MAKE TABLE B) CREATE TABLE C) NEW TABLE D) INSERT TABLE
Answer: B) CREATE TABLE
32. Which command changes the structure of an existing table?
A) UPDATE B) ALTER C) SELECT D) INSERT
Answer: B) ALTER
33. Which command removes a table and its definition?
A) DELETE B) DROP C) UPDATE D) SELECT
Answer: B) DROP
34. Which command removes all rows from a table while keeping its structure?
A) DROP B) TRUNCATE C) ALTER D) CREATE
Answer: B) TRUNCATE
35. Which constraint checks whether values satisfy a condition?
A) CHECK B) DEFAULT C) UNIQUE D) ORDER
Answer: A) CHECK
36. Which constraint provides a value when none is specified during insertion?
A) NOT NULL B) DEFAULT C) UNIQUE D) PRIMARY KEY
Answer: B) DEFAULT
37. Which SQL command is used to give a user database permissions?
A) GRANT B) SELECT C) INSERT D) UPDATE
Answer: A) GRANT
38. Which SQL command removes granted permissions?
A) DELETE B) REVOKE C) DROP D) REMOVE
Answer: B) REVOKE
39. Which command changes the values of existing rows?
A) ALTER B) UPDATE C) CREATE D) GRANT
Answer: B) UPDATE
40. Which command is used to retrieve every column from a table?
A) SELECT ALL FROM table; B) SELECT * FROM table; C) GET * FROM table; D) DISPLAY table;
Answer: B) SELECT * FROM table;
Part 5: Normalization (41–50)
41. What is normalization?
A) Organizing database tables to reduce redundancy and anomalies B) Encrypting database records C) Sorting rows alphabetically D) Deleting every duplicate row manually
Answer: A) Organizing database tables to reduce redundancy and anomalies
42. What does 1NF stand for?
A) First Normal Form B) First Network Function C) File Normal Format D) First Numeric Form
Answer: A) First Normal Form
43. Which normal form requires each field to contain a single value in the relational model?
A) 1NF B) 2NF C) 3NF D) 4NF
Answer: A) 1NF
44. Which normal form eliminates partial functional dependency on a candidate key?
A) 1NF B) 2NF C) 3NF D) 4NF
Answer: B) 2NF
45. Which normal form addresses transitive dependencies of non-key attributes on keys?
A) 1NF B) 2NF C) 3NF D) 5NF
Answer: C) 3NF
46. What is database redundancy?
A) Unnecessary duplication of data B) Data encryption C) Data backup D) Data sorting
Answer: A) Unnecessary duplication of data
47. Which problem can result from storing repeated data in a poorly designed table?
A) Update anomaly B) Faster compilation C) Better encryption D) Automatic indexing
Answer: A) Update anomaly
48. What is denormalization?
A) Deliberately introducing redundancy to improve certain read-performance needs B) Removing all database tables C) Converting SQL into Python D) Deleting all indexes
Answer: A) Deliberately introducing redundancy to improve certain read-performance needs
49. Which normal form deals with multivalued dependencies?
A) 1NF B) 2NF C) 3NF D) 4NF
Answer: D) 4NF
50. What is the main goal of normalization?
A) Reduce unnecessary redundancy and improve data integrity B) Increase duplicate data C) Remove all relationships D) Prevent database queries
Answer: A) Reduce unnecessary redundancy and improve data integrity
Part 6: Joins and Relationships (51–60)
51. What is a JOIN in SQL?
A) An operation that combines related rows from tables B) A command that deletes tables C) A database backup operation D) A type of constraint
Answer: A) An operation that combines related rows from tables
52. Which JOIN returns only rows that satisfy the join condition in both tables?
A) INNER JOIN B) LEFT JOIN C) CROSS JOIN D) FULL OUTER JOIN
Answer: A) INNER JOIN
53. Which JOIN returns all rows from the left table and matching rows from the right table?
A) INNER JOIN B) LEFT JOIN C) CROSS JOIN D) SELF JOIN
Answer: B) LEFT JOIN
54. Which JOIN produces combinations of rows from both tables?
A) INNER JOIN B) LEFT JOIN C) CROSS JOIN D) RIGHT JOIN
Answer: C) CROSS JOIN
55. What is a SELF JOIN?
A) Joining a table with itself B) Joining a table with a file C) Joining two databases without a condition D) Deleting duplicate tables
Answer: A) Joining a table with itself
56. Which relationship connects one record in a table to many records in another table?
A) One-to-one B) One-to-many C) Many-to-none D) Zero-to-zero
Answer: B) One-to-many
57. Which relationship allows many records in one table to relate to many records in another?
A) One-to-one B) One-to-many C) Many-to-many D) One-to-zero
Answer: C) Many-to-many
58. What is a common way to implement a many-to-many relationship in a relational database?
A) Use a junction table B) Remove all primary keys C) Store all data in one cell D) Use only a CHECK constraint
Answer: A) Use a junction table
59. What is a RIGHT JOIN designed to return?
A) All rows from the right table and matching rows from the left B) Only unmatched rows from both tables C) All rows from the left table only D) Only identical table definitions
Answer: A) All rows from the right table and matching rows from the left
60. What is an alias in SQL?
A) A temporary name for a table or column in a query B) A permanent database backup C) A type of primary key D) A command to delete a column
Answer: A) A temporary name for a table or column in a query
Part 7: Transactions and ACID Properties (61–70)
61. What is a database transaction?
A) A logical unit of database work B) A table column C) A database password D) A sorting method
Answer: A) A logical unit of database work
62. What does ACID stand for?
A) Atomicity, Consistency, Isolation, Durability B) Accuracy, Control, Integrity, Data C) Access, Consistency, Indexing, Deletion D) Atomicity, Calculation, Input, Design
Answer: A) Atomicity, Consistency, Isolation, Durability
63. What does atomicity mean?
A) A transaction happens completely or not at all B) A transaction must always run slowly C) Data must always be sorted D) Every table must have two keys
Answer: A) A transaction happens completely or not at all
64. What does consistency ensure?
A) Transactions preserve database rules and valid states B) Every query returns identical rows C) All data is stored in one table D) Every transaction must be read-only
Answer: A) Transactions preserve database rules and valid states
65. What does isolation help prevent?
A) Interference between concurrent transactions B) Table creation C) Data retrieval D) Database backups
Answer: A) Interference between concurrent transactions
66. What does durability mean?
A) Committed changes persist despite subsequent failures covered by the system's guarantees B) Data is automatically deleted after each query C) Transactions cannot be committed D) Tables cannot be modified
Answer: A) Committed changes persist despite subsequent failures covered by the system's guarantees
67. Which SQL command saves a transaction's changes?
A) ROLLBACK B) COMMIT C) REVOKE D) DROP
Answer: B) COMMIT
68. Which command undoes uncommitted transaction changes?
A) COMMIT B) GRANT C) ROLLBACK D) SELECT
Answer: C) ROLLBACK
69. Which command can establish a named point within a transaction to roll back to later?
A) SAVEPOINT B) CHECKPOINT TABLE C) CREATE INDEX D) GROUP BY
Answer: A) SAVEPOINT
70. What is concurrency control?
A) Managing simultaneous database operations to preserve correctness B) Deleting all concurrent users C) Converting tables into images D) Sorting every query result
Answer: A) Managing simultaneous database operations to preserve correctness
Part 8: Indexing and Database Architecture (71–80)
71. What is a database index used for?
A) Speeding up data retrieval for suitable queries B) Encrypting every record C) Deleting duplicate tables D) Replacing all primary keys
Answer: A) Speeding up data retrieval for suitable queries
72. Which data structure is commonly used to implement database indexes?
A) B-tree or B+ tree B) Stack only C) Queue only D) Graph coloring
Answer: A) B-tree or B+ tree
73. What is a disadvantage of creating too many indexes?
A) They can increase storage use and slow writes B) They always delete data C) They prevent SELECT queries D) They remove foreign keys
Answer: A) They can increase storage use and slow writes
74. What is a database schema?
A) The logical structure or definition of a database B) A single row in a table C) A database password D) A backup file only
Answer: A) The logical structure or definition of a database
75. What is metadata?
A) Data that describes other data B) Data that has no meaning C) Only image data D) Deleted database records
Answer: A) Data that describes other data
76. Which component is responsible for processing SQL queries in a DBMS?
A) Query processor B) Keyboard driver C) Web browser D) Image editor
Answer: A) Query processor
77. What is a database view?
A) A virtual table defined by a query B) A physical monitor screen C) A database backup D) A type of transaction log only
Answer: A) A virtual table defined by a query
78. What is a distributed database?
A) A database whose data is stored across multiple connected locations or systems B) A database with only one row C) A database without tables D) A database that cannot communicate over a network
Answer: A) A database whose data is stored across multiple connected locations or systems
79. What is a database administrator (DBA) responsible for?
A) Managing database security, maintenance, access, and performance B) Designing posters only C) Writing operating systems only D) Replacing every database table daily
Answer: A) Managing database security, maintenance, access, and performance
80. Which architecture separates the user interface, application logic, and database into three layers?
A) Two-tier architecture B) Three-tier architecture C) Single-file architecture D) Flat-file architecture
Answer: B) Three-tier architecture
Part 9: ER Model and Relational Concepts (81–90)
81. What does ER stand for in database design?
A) Entity Relationship B) External Record C) Electronic Retrieval D) Entry Reference
Answer: A) Entity Relationship
82. What is an entity?
A) A distinguishable real-world object or concept about which data is stored B) A SQL command C) A database password D) A sorting operation
Answer: A) A distinguishable real-world object or concept about which data is stored
83. What is an attribute in an ER model?
A) A property of an entity B) A database transaction C) A complete database server D) A relationship diagram only
Answer: A) A property of an entity
84. In a standard ER diagram, which shape represents an entity?
A) Rectangle B) Diamond C) Oval D) Triangle
Answer: A) Rectangle
85. In a standard ER diagram, which shape represents a relationship?
A) Circle B) Diamond C) Rectangle D) Hexagon
Answer: B) Diamond
86. What is a tuple in the relational model?
A) A row in a relation B) A column name only C) A database user D) A query plan
Answer: A) A row in a relation
87. What is the degree of a relation?
A) Number of attributes (columns) B) Number of rows C) Number of databases D) Number of transactions
Answer: A) Number of attributes (columns)
88. What is the cardinality of a relation?
A) Number of tuples (rows) B) Number of columns C) Number of keys only D) Number of tables in a server
Answer: A) Number of tuples (rows)
89. Which relational algebra operation selects rows that satisfy a condition?
A) Selection B) Projection C) Union D) Rename
Answer: A) Selection
90. Which relational algebra operation selects specific columns?
A) Selection B) Projection C) Join only D) Difference only
Answer: B) Projection
Part 10: Advanced DBMS and SQL (91–100)
91. What is a stored procedure?
A) A stored collection of SQL statements or procedural logic that can be invoked B) A database table row C) A primary key D) A backup device
Answer: A) A stored collection of SQL statements or procedural logic that can be invoked
92. What is a trigger in a database?
A) Code that automatically executes in response to specified database events B) A command that always deletes a table C) A type of database key D) A manual backup file
Answer: A) Code that automatically executes in response to specified database events
93. Which SQL operator checks whether a value matches any value in a specified list?
A) BETWEEN B) IN C) LIKE D) IS NULL
Answer: B) IN
94. Which SQL operator is commonly used for pattern matching?
A) MATCHES ONLY B) LIKE C) EQUALS D) PATTERN
Answer: B) LIKE
95. In SQL LIKE patterns, what does % usually represent?
A) Exactly one character B) Zero or more characters C) A numeric value only D) A NULL value
Answer: B) Zero or more characters
96. Which clause filters groups after aggregation?
A) WHERE B) HAVING C) ORDER BY D) FROM
Answer: B) HAVING
97. Which function calculates the average of numeric values?
A) SUM() B) COUNT() C) AVG() D) MAX()
Answer: C) AVG()
98. Which SQL expression checks whether a value is NULL?
A) = NULL B) IS NULL C) == NULL D) EQUAL NULL
Answer: B) IS NULL
99. Which command is commonly used to create an index?
A) MAKE INDEX B) CREATE INDEX C) ADD KEY INDEX D) INSERT INDEX
Answer: B) CREATE INDEX
100. Which type of database is designed primarily to store data as documents, key-value pairs, graphs, or other non-relational models?
A) NoSQL database B) Spreadsheet only C) Flat text editor D) Operating system
Answer: A) NoSQL database

Part 1: Python Basics (1–10)
1. Who developed Python?
A) Dennis Ritchie B) Guido van Rossum C) James Gosling D) Bjarne Stroustrup
Answer: B) Guido van Rossum
2. Which extension is used for Python files?
A) .java B) .cpp C) .py D) .html
Answer: C) .py
3. Which function displays output in Python?
A) echo() B) print() C) display() D) show()
Answer: B) print()
4. Which symbol is used for a single-line comment in Python?
A) // B) /* C) # D) --
Answer: C) #
5. Is Python case-sensitive?
A) Yes B) No C) Only for variables D) Only for functions
Answer: A) Yes
6. Which keyword defines a function in Python?
A) function B) def C) fun D) define
Answer: B) def
7. Which of the following is a valid variable name?
A) 2name B) my-name C) my_name D) class
Answer: C) my_name
8. Which function accepts input from the user?
A) scan() B) input() C) read() D) get()
Answer: B) input()
9. Which keyword is used to check a condition?
A) if B) for C) def D) import
Answer: A) if
10. What is the output of print(2 + 3)?
A) 23 B) 5 C) 6 D) Error
Answer: B) 5
Part 2: Data Types and Operators (11–20)
11. Which data type stores whole numbers?
A) str B) int C) list D) bool
Answer: B) int
12. What is the data type of 3.14?
A) int B) str C) float D) bool
Answer: C) float
13. Which data type stores True or False?
A) bool B) int C) str D) float
Answer: A) bool
14. What is the output of 10 // 3?
A) 3.33 B) 3 C) 1 D) 4
Answer: B) 3
15. What is the output of 10 % 3?
A) 3 B) 0 C) 1 D) 10
Answer: C) 1
16. Which operator is used for exponentiation?
A) ^ B) ** C) // D) %
Answer: B) **
17. What is the output of 2 ** 3?
A) 5 B) 6 C) 8 D) 9
Answer: C) 8
18. Which operator checks equality?
A) = B) == C) != D) >=
Answer: B) ==
19. What is the output of 5 != 3?
A) True B) False C) 5 D) Error
Answer: A) True
20. Which function returns the data type of a value?
A) type() B) datatype() C) typeof() D) kind()
Answer: A) type()
Part 3: Strings (21–30)
21. Which of the following creates a string?
A) "Hello" B) 123 C) True D) [1, 2]
Answer: A) "Hello"
22. What is the output of len("Python")?
A) 5 B) 6 C) 7 D) 8
Answer: B) 6
23. What is the output of "Python"[0]?
A) P B) y C) n D) Error
Answer: A) P
24. Which method converts a string to uppercase?
A) upper() B) uppercase() C) capital() D) up()
Answer: A) upper()
25. What is the output of "HELLO".lower()?
A) HELLO B) Hello C) hello D) Error
Answer: C) hello
26. Which operator joins two strings?
A) - B) + C) / D) %
Answer: B) +
27. What is the output of "Py" * 3?
A) Py3 B) PyPyPy C) Py Py Py D) Error
Answer: B) PyPyPy
28. Which method removes whitespace from both ends of a string?
A) strip() B) remove() C) delete() D) clear()
Answer: A) strip()
29. What is the output of "Python"[1:4]?
A) Pyt B) yth C) tho D) ytho
Answer: B) yth
30. Are Python strings mutable?
A) Yes B) No C) Only numeric strings D) Only empty strings
Answer: B) No
Part 4: Lists and Tuples (31–40)
31. Which brackets are used to create a list?
A) () B) {} C) [] D) <>
Answer: C) []
32. Which method adds an element to the end of a list?
A) add() B) append() C) insert_end() D) push()
Answer: B) append()
33. What is the output of len([10, 20, 30])?
A) 2 B) 3 C) 10 D) 60
Answer: B) 3
34. Which method removes an element by its value from a list?
A) remove() B) delete() C) discard() D) erase()
Answer: A) remove()
35. Which method sorts a list in place?
A) order() B) sort() C) arrange() D) sorted_in()
Answer: B) sort()
36. Which brackets are commonly used to create a tuple?
A) [] B) {} C) () D) <>
Answer: C) ()
37. Are tuples mutable?
A) Yes B) No C) Only integers are mutable D) Only strings are mutable
Answer: B) No
38. What is the output of [1, 2, 3][1]?
A) 1 B) 2 C) 3 D) Error
Answer: B) 2
39. Which method adds an element at a specified position in a list?
A) append() B) insert() C) extend() D) sort()
Answer: B) insert()
40. What is the output of list(range(3))?
A) [1, 2, 3] B) [0, 1, 2] C) [0, 1, 2, 3] D) [3]
Answer: B) [0, 1, 2]
Part 5: Dictionaries and Sets (41–50)
41. Which data structure stores key-value pairs?
A) List B) Tuple C) Dictionary D) String
Answer: C) Dictionary
42. Which brackets are used to create a dictionary?
A) [] B) {} C) () D) <>
Answer: B) {}
43. Which method returns a dictionary's keys?
A) keys() B) values() C) items() D) getkeys()
Answer: A) keys()
44. Which method returns a dictionary's values?
A) keys() B) values() C) items() D) get()
Answer: B) values()
45. Which data structure stores unique elements?
A) List B) Tuple C) Set D) String
Answer: C) Set
46. Which operator finds the intersection of two sets?
A) | B) & C) + D) //
Answer: B) &
47. What is the output of len({1, 2, 2, 3})?
A) 2 B) 3 C) 4 D) Error
Answer: B) 3
48. Which dictionary method safely retrieves a key's value with an optional default?
A) fetch() B) get() C) find() D) search()
Answer: B) get()
49. Can a Python dictionary have duplicate keys?
A) Yes, all keys remain separately B) No, keys must be unique C) Only string keys can repeat D) Only integer keys can repeat
Answer: B) No, keys must be unique
50. Which method adds one element to a set?
A) append() B) insert() C) add() D) push()
Answer: C) add()
Part 6: Conditional Statements and Loops (51–60)
51. Which keyword starts an alternative condition after if?
A) else if B) elif C) elseif D) otherwise
Answer: B) elif
52. Which loop iterates over a sequence?
A) for B) switch C) case D) define
Answer: A) for
53. Which loop continues while a condition is True?
A) for B) while C) if D) def
Answer: B) while
54. What does break do inside a loop?
A) Skips only the current iteration B) Terminates the nearest enclosing loop C) Restarts the loop D) Pauses the program permanently
Answer: B) Terminates the nearest enclosing loop
55. What does continue do?
A) Ends the entire program B) Skips to the next iteration C) Deletes the loop D) Returns a value
Answer: B) Skips to the next iteration
56. What is the output of list(range(1, 5))?
A) [1, 2, 3, 4] B) [1, 2, 3, 4, 5] C) [0, 1, 2, 3, 4] D) [5]
Answer: A) [1, 2, 3, 4]
57. How many times does this loop execute? for i in range(4):
A) 3 B) 4 C) 5 D) Infinite times
Answer: B) 4
58. What is the output of print(5 > 3)?
A) True B) False C) 5 D) Error
Answer: A) True
59. Which keyword combines two conditions so both must be True?
A) or B) not C) and D) is
Answer: C) and
60. What does pass do in Python?
A) Exits the program B) Acts as a placeholder without performing an operation C) Skips all future loops D) Returns a value
Answer: B) Acts as a placeholder without performing an operation
Part 7: Functions and Modules (61–70)
61. Which keyword returns a value from a function?
A) print B) return C) yield_value D) send
Answer: B) return
62. What is the output of this code?
def add(a, b):    return a + bprint(add(2, 3))
A) 23 B) 5 C) 6 D) None
Answer: B) 5
63. Which keyword imports a module?
A) include B) using C) import D) require
Answer: C) import
64. Which module provides mathematical functions such as sqrt()?
A) random B) math C) os D) sys
Answer: B) math
65. What is a parameter in a function?
A) A variable listed in the function definition B) A comment C) A loop D) A module name only
Answer: A) A variable listed in the function definition
66. What is a lambda function?
A) An anonymous function defined using lambda B) A class constructor C) A type of loop D) A file-handling method
Answer: A) An anonymous function defined using lambda
67. What is recursion?
A) A function calling itself B) A loop that never stops C) A variable changing type D) A module importing itself only
Answer: A) A function calling itself
68. Which built-in function returns the largest item in an iterable?
A) top() B) max() C) large() D) highest()
Answer: B) max()
69. Which built-in function calculates the sum of items in an iterable?
A) total() B) add_all() C) sum() D) count()
Answer: C) sum()
70. What is the output of abs(-10)?
A) -10 B) 0 C) 10 D) Error
Answer: C) 10
Part 8: Object-Oriented Programming (71–80)
71. Which keyword defines a class in Python?
A) object B) class C) struct D) define
Answer: B) class
72. What is an object?
A) An instance of a class B) A comment C) A loop condition D) A module import
Answer: A) An instance of a class
73. Which method is commonly used to initialize an object's attributes?
A) __start__() B) __init__() C) __create__() D) __main__()
Answer: B) __init__()
74. What does self usually refer to in an instance method?
A) The current instance B) The parent module C) The class name as a string D) A global variable
Answer: A) The current instance
75. What is inheritance?
A) One class deriving attributes and methods from another class B) A function calling itself C) A list storing multiple values D) A variable changing its value
Answer: A) One class deriving attributes and methods from another class
76. What is polymorphism?
A) The ability to use a common interface with different implementations B) The process of deleting objects C) The conversion of strings to integers only D) A type of loop
Answer: A) The ability to use a common interface with different implementations
77. Which concept combines data and the methods that operate on it within a class?
A) Encapsulation B) Iteration C) Compilation D) Recursion
Answer: A) Encapsulation
78. Which function checks whether an object is an instance of a class or type?
A) typecheck() B) isinstance() C) checktype() D) objectof()
Answer: B) isinstance()
79. Which symbol is used to inherit from a base class in a class definition?
A) Square brackets [] B) Parentheses () C) Curly braces {} D) Angle brackets <>
Answer: B) Parentheses ()
80. What is method overriding?
A) A subclass providing its own implementation of an inherited method B) Defining a variable twice C) Calling a function without arguments D) Deleting a class
Answer: A) A subclass providing its own implementation of an inherited method
Part 9: Exceptions and File Handling (81–90)
81. Which keyword is used to handle exceptions?
A) catch B) except C) error D) handle
Answer: B) except
82. Which block contains code that may raise an exception?
A) try B) except C) finally D) else only
Answer: A) try
83. Which block generally executes whether an exception occurs or not?
A) try B) except C) finally D) raise
Answer: C) finally
84. Which keyword manually raises an exception?
A) throw B) raise C) error D) except
Answer: B) raise
85. Which function opens a file in Python?
A) file() B) open() C) readfile() D) load()
Answer: B) open()
86. Which file mode is used to read a file?
A) "w" B) "a" C) "r" D) "x"
Answer: C) "r"
87. Which file mode overwrites an existing file or creates a new one?
A) "r" B) "w" C) "a" D) "b"
Answer: B) "w"
88. Which method reads the entire remaining contents of a file?
A) read() B) write() C) close() D) append()
Answer: A) read()
89. Why is the with open(...) statement useful?
A) It automatically closes the file when the block exits B) It always deletes the file C) It prevents all exceptions D) It converts files into lists automatically
Answer: A) It automatically closes the file when the block exits
90. Which exception is raised when dividing an integer by zero?
A) ValueError B) NameError C) ZeroDivisionError D) TypeError
Answer: C) ZeroDivisionError
Part 10: Advanced Python and Output Questions (91–100)
91. What is the output of print(bool(0))?
A) True B) False C) 0 D) None
Answer: B) False
92. What is the output of print(bool("Hello"))?
A) True B) False C) Hello D) Error
Answer: A) True
93. Which keyword creates a generator function that produces values one at a time?
A) return B) yield C) generate D) next
Answer: B) yield
94. What does enumerate() commonly provide when iterating over a sequence?
A) Only the last element B) Index-value pairs C) Sorted values D) Unique values only
Answer: B) Index-value pairs
95. What is the output of print(10 == 10.0)?
A) True B) False C) 10 D) Error
Answer: A) True
96. Which expression creates a list of squares from 0 to 4?
A) [x**2 for x in range(5)] B) {x**2 for x in range(5)} C) (x**2 for x in range(5)) D) x**2 in range(5)
Answer: A) [x**2 for x in range(5)]
97. What is the output of print("Python"[::-1])?
A) Python B) nohtyP C) P D) Error
Answer: B) nohtyP
98. Which keyword is used to create an asynchronous function?
A) async B) await C) parallel D) thread
Answer: A) async
99. What is the output of print([1, 2] + [3, 4])?
A) [4, 6] B) [1, 2, 3, 4] C) [[1, 2], [3, 4]] D) Error
Answer: B) [1, 2, 3, 4]
100. What is the output of the following code?
x = [1, 2, 3]x.append(4)print(x)
A) [1, 2, 3] B) [4, 1, 2, 3] C) [1, 2, 3, 4] D) 4
Answer: C) [1, 2, 3, 4]

Part 1: Data Structures Basics (1–10)
1. What is a data structure?
A) A programming language B) A way to organize and store data C) An operating system D) A computer network
Answer: B) A way to organize and store data
2. Which of the following is a linear data structure?
A) Tree B) Graph C) Array D) Heap
Answer: C) Array
3. Which data structure follows LIFO?
A) Queue B) Stack C) Tree D) Graph
Answer: B) Stack
4. Which data structure follows FIFO?
A) Stack B) Queue C) Tree D) Heap
Answer: B) Queue
5. Which of the following is a non-linear data structure?
A) Array B) Stack C) Queue D) Tree
Answer: D) Tree
6. What is the main advantage of an array?
A) Random access to elements B) Unlimited size in every language C) No memory usage D) Automatic sorting
Answer: A) Random access to elements
7. Which data structure stores elements in nodes connected by pointers or references?
A) Array B) Linked list C) Matrix D) String
Answer: B) Linked list
8. Which operation adds an element to a data structure?
A) Delete B) Search C) Insert D) Traverse
Answer: C) Insert
9. Which operation visits each element of a data structure?
A) Traversal B) Compilation C) Encryption D) Recursion
Answer: A) Traversal
10. What does time complexity describe?
A) Memory capacity B) Execution time growth as input size increases C) Program file size D) Number of variables
Answer: B) Execution time growth as input size increases
Part 2: Arrays (11–20)
11. In most programming languages, what is the index of the first array element?
A) 0 B) 1 C) -1 D) 2
Answer: A) 0
12. What is the time complexity of accessing an array element by index?
A) O(n) B) O(log n) C) O(1) D) O(n²)
Answer: C) O(1)
13. Which of the following best describes an array?
A) A collection of elements accessed using indices B) A collection of unrelated programs C) A type of operating system D) A network protocol
Answer: A) A collection of elements accessed using indices
14. What is the time complexity of linear search in an unsorted array in the worst case?
A) O(1) B) O(log n) C) O(n) D) O(n²)
Answer: C) O(n)
15. Inserting an element at the beginning of an array usually requires what?
A) Shifting existing elements B) Deleting the entire array C) Sorting all elements D) Reversing the array
Answer: A) Shifting existing elements
16. Which array type uses rows and columns?
A) One-dimensional array B) Two-dimensional array C) Circular array only D) Linked array
Answer: B) Two-dimensional array
17. What is a major limitation of a traditional fixed-size array?
A) It cannot store numbers B) Its capacity is fixed after creation C) It cannot be indexed D) It cannot be traversed
Answer: B) Its capacity is fixed after creation
18. What is the index of the last element in an array of size 10 with zero-based indexing?
A) 10 B) 9 C) 11 D) 0
Answer: B) 9
19. Which operation finds the total number of elements in an array?
A) Length or size check B) Sorting C) Reversing D) Merging
Answer: A) Length or size check
20. Which of the following is commonly used to represent a table of values?
A) Stack B) Two-dimensional array C) Queue D) Binary tree
Answer: B) Two-dimensional array
Part 3: Linked Lists (21–30)
21. What is a linked list?
A) A collection of connected nodes B) A collection of fixed-size tables C) A sorting technique D) A searching algorithm
Answer: A) A collection of connected nodes
22. Which fields are commonly present in a singly linked list node?
A) Data and next pointer B) Data and two arrays C) Index and stack D) Key and queue
Answer: A) Data and next pointer
23. Which pointer points to the first node of a linked list?
A) Tail B) Head C) Root D) Rear
Answer: B) Head
24. Which linked list allows traversal in both directions?
A) Singly linked list B) Doubly linked list C) Circular queue D) Simple array
Answer: B) Doubly linked list
25. In a singly linked list, what does the last node's next pointer usually contain?
A) Head B) Root C) NULL D) Previous node
Answer: C) NULL
26. What is the time complexity of accessing the nth element in a singly linked list?
A) O(1) B) O(log n) C) O(n) D) O(n²)
Answer: C) O(n)
27. Which linked list connects the last node back to the first node?
A) Circular linked list B) Linear linked list C) Doubly linked list only D) Static array
Answer: A) Circular linked list
28. What is a major advantage of linked lists over fixed-size arrays?
A) Constant-time random access B) Flexible size C) Always use less memory D) Automatic sorting
Answer: B) Flexible size
29. What is generally required to insert a node at the beginning of a singly linked list?
A) Updating the head pointer B) Sorting the list C) Shifting every node D) Deleting the last node
Answer: A) Updating the head pointer
30. Which of the following is a disadvantage of a linked list?
A) It cannot store data B) It does not support direct random access C) It cannot grow dynamically D) It cannot be traversed
Answer: B) It does not support direct random access
Part 4: Stacks (31–40)
31. Which operation inserts an element into a stack?
A) Enqueue B) Push C) Dequeue D) Search
Answer: B) Push
32. Which operation removes the top element from a stack?
A) Pop B) Push C) Insert D) Traverse
Answer: A) Pop
33. What is stack overflow?
A) Removing an element from an empty stack B) Adding an element to a full bounded stack C) Sorting a stack D) Searching a stack
Answer: B) Adding an element to a full bounded stack
34. What is stack underflow?
A) Pushing an element onto a stack B) Creating a stack C) Attempting to pop from an empty stack D) Reversing a stack
Answer: C) Attempting to pop from an empty stack
35. Which data structure is commonly used to manage function calls?
A) Stack B) Queue C) Graph D) Hash table
Answer: A) Stack
36. Which application commonly uses a stack?
A) Undo operation in a text editor B) Printer scheduling only C) Network routing only D) Database table creation
Answer: A) Undo operation in a text editor
37. What is the time complexity of push in a stack implemented using an array, assuming space is available?
A) O(n) B) O(log n) C) O(1) D) O(n²)
Answer: C) O(1)
38. Which data structure is often used to check balanced parentheses?
A) Stack B) Queue C) Graph D) Heap
Answer: A) Stack
39. Which element is removed first from the stack containing 10, 20, 30, pushed in that order?
A) 10 B) 20 C) 30 D) All at once
Answer: C) 30
40. Which algorithm technique commonly uses a stack to manage unfinished work?
A) Depth-first search B) Breadth-first search C) Counting sort only D) Hashing only
Answer: A) Depth-first search
Part 5: Queues (41–50)
41. Which operation adds an element to a queue?
A) Push B) Enqueue C) Pop D) Peek
Answer: B) Enqueue
42. Which operation removes an element from a queue?
A) Dequeue B) Push C) Insert at top D) Peek
Answer: A) Dequeue
43. In a standard queue, insertion usually occurs at the:
A) Front B) Rear C) Middle D) Top
Answer: B) Rear
44. In a standard queue, deletion usually occurs at the:
A) Rear B) Middle C) Front D) Top
Answer: C) Front
45. What is a circular queue?
A) A queue that connects its final position back to its first position logically B) A queue that stores only circular objects C) A stack arranged in a circle D) A queue that cannot delete elements
Answer: A) A queue that connects its final position back to its first position logically
46. Which queue type allows insertion and deletion at both ends?
A) Simple queue B) Deque C) Priority stack D) Binary queue only
Answer: B) Deque
47. Which data structure is commonly used in breadth-first search (BFS)?
A) Stack B) Queue C) Heap only D) Hash table only
Answer: B) Queue
48. Which is a common real-world application of a queue?
A) Managing print jobs B) Function call management C) Expression parentheses checking only D) Recursive function tracking
Answer: A) Managing print jobs
49. What is a priority queue?
A) A queue where elements are served according to priority B) A queue where only the last element is removed C) A stack with no top element D) A queue that cannot store numbers
Answer: A) A queue where elements are served according to priority
50. What is the time complexity of enqueue in a typical queue implemented with a linked list and a rear pointer?
A) O(n) B) O(log n) C) O(1) D) O(n²)
Answer: C) O(1)
Part 6: Trees and Binary Trees (51–60)
51. What is a tree in data structures?
A) A linear collection of elements B) A hierarchical collection of nodes C) A sorting algorithm D) A type of array
Answer: B) A hierarchical collection of nodes
52. What is the topmost node of a tree called?
A) Leaf B) Root C) Edge D) Child
Answer: B) Root
53. What is a leaf node?
A) A node with no children B) A node with two parents C) The topmost node D) A node without data
Answer: A) A node with no children
54. In a binary tree, each node can have at most how many children?
A) 1 B) 2 C) 3 D) 4
Answer: B) 2
55. Which traversal visits the root before its left and right subtrees?
A) Inorder B) Postorder C) Preorder D) Level-order
Answer: C) Preorder
56. Which traversal follows Left–Root–Right?
A) Preorder B) Inorder C) Postorder D) Level-order
Answer: B) Inorder
57. Which traversal follows Left–Right–Root?
A) Preorder B) Inorder C) Postorder D) Level-order
Answer: C) Postorder
58. What is a Binary Search Tree (BST)?
A) A tree where every node must have exactly two children B) A binary tree ordered by key values according to BST rules C) A tree used only for graphics D) A tree without leaf nodes
Answer: B) A binary tree ordered by key values according to BST rules
59. In a BST with distinct keys, where are keys smaller than a node's key placed?
A) In its left subtree B) In its right subtree C) Always at the root D) Outside the tree
Answer: A) In its left subtree
60. Which data structure is commonly used to perform level-order traversal of a tree?
A) Stack B) Queue C) Hash table D) Array index only
Answer: B) Queue
Part 7: Graphs (61–70)
61. What is a graph made up of?
A) Rows and columns only B) Vertices and edges C) Stacks and queues only D) Roots and leaves only
Answer: B) Vertices and edges
62. What is a vertex in a graph?
A) A node B) A sorting method C) A pointer only D) A queue operation
Answer: A) A node
63. What connects two vertices in a graph?
A) Index B) Edge C) Root D) Stack
Answer: B) Edge
64. What is a directed graph?
A) A graph whose edges have directions B) A graph without vertices C) A graph with no edges D) A graph that must be a tree
Answer: A) A graph whose edges have directions
65. Which algorithm is commonly used for breadth-first search in a graph?
A) BFS B) DFS C) Binary search D) Insertion sort
Answer: A) BFS
66. Which data structure is commonly used for iterative depth-first search?
A) Queue B) Stack C) Priority queue only D) Hash table only
Answer: B) Stack
67. Which representation stores a list of neighboring vertices for each vertex?
A) Adjacency list B) Stack array C) Sorted array D) Linked stack only
Answer: A) Adjacency list
68. Which graph representation uses a two-dimensional table of vertex connections?
A) Linked list B) Adjacency matrix C) Binary tree D) Circular queue
Answer: B) Adjacency matrix
69. What is a path in a graph?
A) A sequence of connected vertices B) A single isolated vertex only C) A sorting operation D) A memory address
Answer: A) A sequence of connected vertices
70. Which algorithm can find shortest paths from a source in a graph with non-negative edge weights?
A) Dijkstra's algorithm B) Bubble sort C) Binary search D) Preorder traversal
Answer: A) Dijkstra's algorithm
Part 8: Searching Algorithms (71–80)
71. Which searching algorithm checks elements one by one?
A) Binary search B) Linear search C) Merge sort D) Heap sort
Answer: B) Linear search
72. What is the worst-case time complexity of linear search in an array of n elements?
A) O(1) B) O(log n) C) O(n) D) O(n log n)
Answer: C) O(n)
73. Binary search generally requires the data to be:
A) Randomly arranged B) Sorted C) Stored in a stack D) Stored only in a tree
Answer: B) Sorted
74. What is the worst-case time complexity of binary search on a sorted array?
A) O(n) B) O(n²) C) O(log n) D) O(1)
Answer: C) O(log n)
75. Binary search works by repeatedly dividing the search interval into how many parts?
A) Two B) Three C) Four D) Ten
Answer: A) Two
76. In binary search, what happens if the target is smaller than the middle element in ascending order?
A) Search the left half B) Search the right half C) Stop immediately with success D) Sort the array again
Answer: A) Search the left half
77. Which search method is generally suitable for a small, unsorted array?
A) Linear search B) Binary search without sorting C) Tree traversal only D) Dijkstra's algorithm
Answer: A) Linear search
78. What is the best-case time complexity of linear search when the target is the first element?
A) O(n) B) O(log n) C) O(1) D) O(n²)
Answer: C) O(1)
79. Which search algorithm repeatedly compares the target with the middle element?
A) Linear search B) Binary search C) Depth-first search D) Breadth-first search
Answer: B) Binary search
80. What is the maximum number of elements checked in the worst case by linear search in an array of 100 elements?
A) 10 B) 50 C) 99 D) 100
Answer: D) 100
Part 9: Sorting Algorithms (81–90)
81. Which sorting algorithm repeatedly swaps adjacent elements when they are in the wrong order?
A) Merge sort B) Bubble sort C) Quick sort D) Heap sort
Answer: B) Bubble sort
82. What is the average time complexity of Quick sort?
A) O(n) B) O(n²) C) O(n log n) D) O(log n)
Answer: C) O(n log n)
83. What is the worst-case time complexity of Bubble sort?
A) O(1) B) O(log n) C) O(n) D) O(n²)
Answer: D) O(n²)
84. Which sorting algorithm uses the divide-and-conquer technique?
A) Merge sort B) Linear search C) Bubble sort only D) Sequential search
Answer: A) Merge sort
85. What is the worst-case time complexity of Merge sort?
A) O(n²) B) O(n log n) C) O(log n) D) O(1)
Answer: B) O(n log n)
86. Which sorting algorithm selects the smallest element from the unsorted portion in each pass?
A) Selection sort B) Merge sort C) Quick sort D) Heap sort
Answer: A) Selection sort
87. Which sorting algorithm builds a sorted portion by inserting each new element into its correct position?
A) Bubble sort B) Insertion sort C) Heap sort D) Counting sort
Answer: B) Insertion sort
88. Which sorting algorithm uses a pivot element to partition the array?
A) Quick sort B) Merge sort C) Selection sort D) Insertion sort
Answer: A) Quick sort
89. Which sorting algorithm uses a heap data structure?
A) Bubble sort B) Heap sort C) Insertion sort D) Linear sort
Answer: B) Heap sort
90. Which sorting algorithm is generally stable and guarantees O(n log n) time in its standard array implementation?
A) Merge sort B) Selection sort C) Quick sort D) Bubble sort
Answer: A) Merge sort
Part 10: Hashing, Heaps and Complexity (91–100)
91. What is hashing used for?
A) Mapping keys to positions or hash values B) Arranging nodes into a tree only C) Reversing an array D) Managing function calls
Answer: A) Mapping keys to positions or hash values
92. What is a hash table?
A) A data structure that stores key-based entries using a hash function B) A sorting algorithm C) A type of linked list only D) A graph traversal method
Answer: A) A data structure that stores key-based entries using a hash function
93. What is a hash collision?
A) When two different keys map to the same hash location B) When an array becomes empty C) When a tree loses its root D) When a stack overflows
Answer: A) When two different keys map to the same hash location
94. Which technique resolves hash collisions by storing multiple entries in a bucket, often using a linked list?
A) Linear search B) Separate chaining C) Binary search D) Merge sort
Answer: B) Separate chaining
95. What is the average-case lookup time of a well-designed hash table under suitable assumptions?
A) O(1) B) O(n²) C) O(log n) D) O(2ⁿ)
Answer: A) O(1)
96. What is a heap in data structures?
A) A complete binary tree that satisfies the heap-order property B) A sorted linked list C) A graph with no edges D) A fixed-size stack
Answer: A) A complete binary tree that satisfies the heap-order property
97. In a max-heap, which element is stored at the root?
A) The smallest element B) The largest element C) The middle element D) The oldest element
Answer: B) The largest element
98. What is the time complexity of inserting an element into a binary heap with n elements?
A) O(1) in all cases B) O(log n) C) O(n²) D) O(2ⁿ)
Answer: B) O(log n)
99. What does O(1) time complexity mean?
A) Execution time grows linearly with input size B) Execution time grows quadratically with input size C) Execution time remains constant with respect to input size D) Execution time doubles with each input element
Answer: C) Execution time remains constant with respect to input size
100. Which data structure is most suitable for implementing a priority queue efficiently?
A) Unsorted string B) Binary heap C) Simple stack D) Two-dimensional array only
Answer: B) Binary heap
"""

def parse_mcqs_by_category(text):
    categories = {
        "Web Development": [],
        "Java": [],
        "DBMS": [],
        "Python": [],
        "DSA": []
    }
    
    current_cat = None
    lines = text.strip().split("\n")
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Detect Category Header
        lower_line = line.lower()
        if "html" in lower_line or "css" in lower_line or "javascript" in lower_line or "frontend" in lower_line or "backend" in lower_line or "http and web" in lower_line or "web security" in lower_line:
            current_cat = "Web Development"
        elif "java basics" in lower_line or "data types and variables" in lower_line and "java" in text[max(0, text.find(line)-200):text.find(line)+200].lower() or "collections framework" in lower_line or "multithreading" in lower_line:
            current_cat = "Java"
        elif "dbms" in lower_line or "sql" in lower_line or "er model" in lower_line or "normalization" in lower_line or "acid" in lower_line:
            current_cat = "DBMS"
        elif "python" in lower_line:
            current_cat = "Python"
        elif "data structures" in lower_line or "stacks" in lower_line or "queues" in lower_line or "trees" in lower_line or "graphs" in lower_line or "searching algorithms" in lower_line or "sorting algorithms" in lower_line or "hashing" in lower_line:
            current_cat = "DSA"
            
        # Check if question line
        q_match = re.match(r"^(\d+)\.\s*(.*)", line)
        if q_match and current_cat:
            q_num = q_match.group(1)
            q_text = q_match.group(2).strip()
            
            # Next line: Options
            i += 1
            opt_line = lines[i].strip() if i < len(lines) else ""
            
            # Next line: Answer
            i += 1
            ans_line = lines[i].strip() if i < len(lines) else ""
            
            # Parse Options: A) ... B) ... C) ... D) ...
            opt_pattern = r"A\)\s*(.*?)\s*B\)\s*(.*?)\s*C\)\s*(.*?)\s*D\)\s*(.*)"
            m_opt = re.match(opt_pattern, opt_line)
            options = []
            if m_opt:
                options = [m_opt.group(1).strip(), m_opt.group(2).strip(), m_opt.group(3).strip(), m_opt.group(4).strip()]
            else:
                # Fallback splitting
                parts = re.split(r"[A-D]\)\s*", opt_line)
                options = [p.strip() for p in parts if p.strip()]
                
            # Parse Answer: Answer: B) ...
            m_ans = re.search(r"Answer:\s*([A-D])\)", ans_line)
            ans_idx = 0
            if m_ans:
                letter = m_ans.group(1).upper()
                ans_idx = ord(letter) - ord('A')
                
            categories[current_cat].append({
                "q": q_text,
                "options": options,
                "answer": ans_idx
            })
        i += 1
        
    return categories

parsed = parse_mcqs_by_category(raw_text)
for cat, qs in parsed.items():
    print(f"Extracted {len(qs)} MCQs for {cat}")

with open("scratch_parsed_mcqs.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=2)

print("Saved parsed MCQs to scratch_parsed_mcqs.json")
