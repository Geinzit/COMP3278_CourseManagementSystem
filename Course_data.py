from django.db import models

from manager.models import Course, Teacher

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    description = models.TextField()

course1 = Course(
    course_id="030815",
    course_name="COMP1117",
    teacher=Teacher.objects.get(name="Dr. Loretta Choi"),
    description="Computer Programming",
    course_information="""Not for students who have passed in ENGG1111 or ENGG1112 or ENGG1330 or IIMT2602, or have already enrolled in these courses

Approved Syllabus
This is an introductory course in computer programming. Students will acquire basic Python programming skills, including syntax, identifiers, control statements, functions, recursions, strings, lists, dictionaries, tuples and files. Searching and sorting algorithms, such as sequential search, binary search, bubble sort, insertion sort and selection sort, will also be covered.
Mutually exclusive with: ENGG1111 or ENGG1330
Assessment: 70% continuous assessment, 30% examination

Course Objectives
By the end of this course students should be able to demonstrate a threshold level of mastery of the following learning outcomes.
[Computational mind]
Able to identify possible solutions for problems based on computer programs.
[Program implementation]
Able to implement solutions for problems using Python
[Program comprehension]
Able to understand programs written by others and participate in larger scale system implementation"""
)

    

course2 = Course(
    course_id="030811",
    course_name="COMP2119",
    teacher=Teacher.objects.get(name="Dr. H.T.H. Chan"),
    description="Introduction to data structures and algorithms",
    course_information="""Prerequisites: Pass in ENGG1340 or COMP2113 or COMP2123

Approved Syllabus
To study data structures and algorithms in the broader context of solving problems using computers. The course includes topics such as arrays, linked lists, trees, and graphs; stacks and queues; symbol tables; priority queues, balanced trees; sorting algorithms; and complexity analysis. The course aims to provide a comprehensive understanding of these fundamental concepts and their applications in computer science.
Assessment: 40% continuous assessment, 60% examination

Course Objectives
By the end of this course, students should be able to demonstrate a threshold level of mastery of the following learning outcomes:
- [Mathematics foundation] Understand the concept of time and space complexity and analyze the time and space complexities of an algorithm and a data structure.
- [Data structures] Understand well-known generic data structures such as stack, queue, tree and related algorithms and apply them to solve problems.
- [Problem solving] Design new data structures and algorithms to solve problems.
- [Implementation] Implement selected data structures and algorithms."""
)

course3 = Course(
    course_id="030812",
    course_name="COMP2120",
    teacher=Teacher.objects.get(name="Dr. Qi Zhao"),
    description="Computer organization",
    course_information="""Prerequisites: Pass in COMP1117 or ENGG1330, or already enrolled in these courses; Mutually exclusive with: ELEC2441

Approved Syllabus
Introduction to computer organization and architecture; data representations; instruction sets; machine and assembly languages; basic logic design and integrated devices; the central processing unit (CPU) and its control; memory and caches; I/O and storage systems; computer arithmetic. This course aims to provide a comprehensive understanding of the hardware organization of computers and how they operate at a fundamental level. Students will gain insights into the detailed operations of computers, particularly through assembly language programming.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
To introduce the hardware organization of computers and detailed operations of computers through assembly language programming. 
The course will cover topics such as computer organization and architecture, data representations, instruction sets, machine and assembly languages, basic logic design and integrated devices, CPU and its control, memory and caches, I/O and storage systems, and computer arithmetic. 
By the end of this course, students will have a solid understanding of how computer systems are organized and operate at a hardware level."""
)

course4 = Course(
    course_id="030810",
    course_name="COMP2121",
    teacher=Teacher.objects.get(name="Dr. H.T.H. Chan"),
    description="Discrete mathematics",
    course_information="""Mutually exclusive with: MATH3600

Approved Syllabus
This course provides students a solid background in discrete mathematics and structures pertinent to computer science. 
Topics include logic, set theory, mathematical reasoning, counting techniques, discrete probability, trees, graphs, and related algorithms, and modeling computation. 
It is designed to introduce mathematical topics essential to computer studies and to develop mathematical maturity in reasoning and analysis.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
The primary goal of this course is to introduce those mathematical topics whose understanding is essential to computer studies and to develop mathematical maturity in reasoning and analysis. 
By the end of this course, students are expected to have a solid foundation in discrete mathematics and an ability to apply this knowledge to computer science topics, including logic, set theory, mathematical reasoning, counting techniques, discrete probability, and the analysis of algorithms."""
)

course5 = Course(
    course_id="030823",
    course_name="COMP2396",
    teacher=Teacher.objects.get(name="Dr. T.W. Chim"),
    description="Object-oriented programming and Java",
    course_information="""Prerequisites: Pass in ENGG1340 or COMP2113 or COMP2123; Mutually exclusive with ELEC2543 or FITE2000

Approved Syllabus
This course provides an introduction to object-oriented programming, focusing on abstract data types, classes, inheritance, polymorphism, and object-oriented program design. 
Students will learn the Java programming language and its development environment, including user interfaces and GUI programming, collection classes, iteration protocols, and program documentation. 
The course aims to equip students with a solid foundation in object-oriented programming concepts and practical skills in Java development.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
The primary goal of this course is to introduce students to object-oriented programming and the Java language. 
By the end of the course, students are expected to understand abstract data types and classes, inheritance and polymorphism, object-oriented program design, and user interfaces and GUI programming in Java. 
They should also be able to effectively use Java's program development environment, work with collection classes and iteration protocols, and properly document their programs."""
)

course6 = Course(
    course_id="037006",
    course_name="COMP2113",
    teacher=Teacher.objects.get(name="Dr. Chenxiong Qian"),
    description="Programming technologies",
    course_information="""Prerequisites: Pass in COMP1117 or ENGG1330; Not for students who have passed in ENGG1340 or COMP2123, or have already enrolled in these courses

Approved Syllabus
This course covers intermediate to advanced computer programming topics focusing on various technologies and tools essential for software development. 
Topics include Linux shell commands, shell scripts, C/C++ programming, separate compilation techniques, and version control. 
As a self-learning course, there will be no lectures, and students will be provided with self-study materials. Milestone-based self-assessment tasks are required throughout the course. This course is designed for students with an interest in Computer Science/Computer Engineering.
Assessment: Written examination (30%), Continuous assessment (70%)

Course Objectives
By the end of this course, students will be able to:
1. Understand and analyse problems and implement solutions using C/C++, utilizing debuggers, separate compilation, makefiles, and version control.
2. Work comfortably on the Linux platform, utilizing its functionalities for program development.
3. Understand and explain advanced programming techniques, including recursion, dynamic memory management, Standard Template Library (STL), data structures, and algorithms.
4. Self-learn various programming techniques and apply them effectively in practical scenarios."""
)

course7 = Course(
    course_id="038210",
    course_name="COMP2501",
    teacher=Teacher.objects.get(name="Dr. Ruibang Luo"),
    description="Introduction to Data Science and Engineering",
    course_information="""Prerequisites: Pass in COMP1117 or ENGG1330; Mutually exclusive with: STAT1005 or STAT1015

Approved Syllabus
The course introduces basic concepts and methodology of data science. 
The goal of this course is to provide students with an overview and practical experience of the entire data analysis process. 
Topics include data source and data acquisition, data preparation and manipulation, exploratory data analysis, statistical and predictive analysis, data visualization, and communication.
Continuous Assessment (50%)
Written Examination (50%)

Course Objectives
By the end of this course, students will:
1. Understand the basic concepts and methodologies of data science.
2. Gain practical experience in the entire data analysis process.
3. Be able to work with data sources and data acquisition, prepare and manipulate data.
4. Perform exploratory data analysis, statistical and predictive analysis.
5. Learn data visualization techniques and effective communication of data insights."""
)

course8 = Course(
    course_id="030816",
    course_name="COMP3230",
    teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"),
    description="Principles of Operating Systems",
    course_information="""Prerequisites: Pass in ENGG1340 or COMP2113 or COMP2123; and COMP2120 or ELEC2441

Approved Syllabus
Operating system structures, process and thread, CPU scheduling, process synchronization, deadlocks, memory management, file systems, I/O systems and device driver, mass-storage structure and disk scheduling, case studies.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
The course aims to present the fundamentals of operating systems and study the detailed operation and principles behind the design of various components of an operating system. 
Topics covered include operating system structures, processes and threads, CPU scheduling, process synchronization, deadlocks, memory management, file systems, I/O systems and device drivers, mass-storage structure and disk scheduling, along with relevant case studies."""
)

course9 = Course(
    course_id="030825",
    course_name="COMP3231",
    teacher=Teacher.objects.get(name="Dr. Heming Cui"),
    description="Computer architecture",
    course_information="""Prerequisites: Pass in COMP2120

Approved Syllabus
This course provides an introduction to the computer design process, including performance and cost analysis, instruction set design, data-path and controller design, pipelining, memory system, I/O design, GPU architecture and programming, and introduction to advanced topics. 
The course serves as a continuation of basic concepts in machine organization, with a focus on architecture – interconnecting and integrating hardware components to form useful systems. Examples are drawn from both conventional and advanced architectures.
Assessment: 40% continuous assessment, 60% examination

Course Objectives
The course aims to extend the understanding of machine organization to include computer architecture. 
It covers the design process of computer systems, the analysis of performance and cost, and the development of instruction sets, data-path and controller designs. 
The course also introduces pipelining, memory systems, I/O design, GPU architecture, and advanced topics, with a focus on how these elements integrate to form complete systems. 
By the end of the course, students should be able to understand and analyze various computer architectures and their components."""
)

course10 = Course(
    course_id="030817",
    course_name="COMP3234",
    teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"),
    description="Computer and Communication Networks",
    course_information="""Prerequisites: Pass in ENGG1340 or COMP2113 or COMP2123 or ELEC2543; and COMP2120 or ELEC2441; Mutually exclusive with: ELEC3443

Approved Syllabus
The course covers network structure and architecture, reference models, protocols like stop and wait, sliding window, character and bit-oriented protocols, virtual circuits and datagrams, routing, flow control, congestion control, local area networks, network interconnection principles, transport protocols, application layer, and examples of network protocols.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
On successful completion of this course, students should be able to:
- Explain key terminologies of computer networks, such as host, links, protocol stack, throughput, etc.
- Describe services and functions of each layer in the Internet protocol stack.
- Describe principles behind network technologies like circuit/packet switching, reliable data transfer, flow/congestion control, routing, multiple access, and protocols like 802.11 WiFi, Ethernet, ARP, IP, TCP, etc.
- Calculate packet delay, throughput, channel efficiency under different network protocols.
- Implement network protocols using Socket Interface, design network applications, and reliable data transfer protocols.
- Plan for IP networks and assign IP addresses in given network scenarios."""
)

course11 = Course(
    course_id="038858",
    course_name="COMP3251",
    teacher=Teacher.objects.get(name="Dr. Zhiyi Huang"),
    description="Algorithm Design",
    course_information="""Prerequisites: Pass in COMP2119; Mutually exclusive with: COMP3250 or COMP3252

Approved Syllabus
The course introduces various algorithm design techniques, including divide and conquer, greedy, and dynamic programming. It covers selected topics in graph algorithms and provides an insight into designing better algorithms for various areas of computer science. Additionally, the course offers an overview of NP-complete problems and their significance in the field of algorithm design.

Course Objectives
By the end of this course, students will:
1. Understand and apply various algorithm design techniques, such as divide and conquer, greedy algorithms, and dynamic programming.
2. Gain knowledge in graph algorithms and their applications.
3. Learn about NP-complete problems and comprehend their importance in computer science.
4. Develop skills to design efficient algorithms for solving complex computational problems."""
)

course12 = Course(
    course_id="033795",
    course_name="COMP3258",
    teacher=Teacher.objects.get(name="Dr. B. Oliveira"),
    description="Functional Programming",
    course_information="""Prerequisites: Pass in COMP2121

Approved Syllabus
This course introduces the basics of functional programming using Haskell. Key concepts include recursion, abstraction, lambda expressions, higher-order functions, and data types. It also covers the mathematical reasoning in functional program design and techniques for proving properties about functions. The course highlights the relevance of functional programming in modern programming languages like Java, C++, and C#. It is crucial for students to learn these techniques to stay updated with the evolving programming paradigms.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
Upon successful completion of this course, students will be able to:
- Implement programs using Functional Programming techniques and Haskell, and use tools like Quickcheck for development.
- Utilize the GHC compiler and the GHCI command line interpreter effectively.
- Analyze and design solutions for problems using functional programming modeling techniques, model data structures as algebraic datatypes, and define operations by pattern matching.
- Understand and explain advanced functional programming techniques such as recursion, datatypes, higher-order functions, functional data structures, and algorithms."""
)

course13 = Course(
    course_id="030828", 
    course_name="COMP3259", 
    teacher=Teacher.objects.get(name="Dr. B. Oliveira"), 
    description="Principles of programming languages",
    course_information = """Pass in COMP2119 or FITE2000

Approved Syllabus
Syntax and semantics specification; data types; data control and memory management; expressions, precedence and associativity of operators; control structures; comparative study of existing programming languages; advanced topics such as polymorphism, programming paradigms, exception handling and concurrency.
Assessment: 40% continuous assessment, 60% examination

Course Objectives
To study the design, specification and implementation of programming languages.
Syntax and semantics specification; data types; data control and memory management; expressions, precedence and associativity of operators; control structures; comparative study of existing programming languages; advanced topics such as polymorphism, programming paradigms, exception handling and concurrency.
On successful completion of the course, students should be able to:
[Programming languages fundamentals] Be able to understand the fundamental principles underlying various programming languages features
[Programming language implementation] Be able to understand the basic algorithms in implementing simple programming languages
[Programming language designs] Be able to understand some principles in the design of programming languages"""
)

course14 = Course(
    course_id="030830", 
    course_name="COMP3270", 
    teacher=Teacher.objects.get(name="Dr. D. Schnieders"), 
    description="Artificial intelligence",
    course_information = """Pass in COMP2119 or FITE2000; Mutually exclusive with: IIMT3688 or ELEC4544

Approved Syllabus
This is an introduction course on the subject of artificial intelligence. Topics include: intelligent agents; search techniques for problem solving; knowledge representation; logical inference; reasoning under uncertainty; statistical models and machine learning.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
This is an introduction course on the subject of artificial intelligence. Topics include: intelligent agents; search techniques for problem solving; knowledge representation; logical inference; reasoning under uncertainty; statistical models and machine learning. This course may not be taken with BUSI0088.
On successful completion of the course, students should be able to:
[1] understand the basic principles and technologies of intelligent computer systems
[2] explain the algorithms to achieve AI
[3] develop some AI programs"""
)

course15 = Course(
    course_id="030814", 
    course_name="COMP3278", 
    teacher=Teacher.objects.get(name="Dr. C.K. Chui"), 
    description="Introduction to database management systems",
    course_information = """Pass in COMP2119 or ELEC2543 or COMP2502 or FITE2000; Mutually exclusive with: IIMT3601

Approved Syllabus
This course studies the principles, design, administration, and implementation of database management systems.  Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control.
On successful completion of the course, students should be able to:
[Information Modeling] Able to understand the modeling of real-life information in a database system.
[Query Languages] Able to understand and use the languages designed for data access.
[System Design] Able to understand the design issues of an efficient and reliable database system.
[Application Development] Able to implement a practical application on a real database."""
)

course16 = Course(
    course_id="030833",
    course_name="COMP3314",
    teacher=Teacher.objects.get(name="Dr. Hengshuang Zhao"),
    description="Machine learning",
    course_information = """Pass in MATH1853 or MATH2014; and COMP2119 or ELEC2543 or FITE2000

Approved Syllabus
This course introduces algorithms, tools, practices, and applications of machine learning. Topics include core methods such as supervised learning (classification and regression), unsupervised learning (clustering, principal component analysis), Bayesian estimation, neural networks; common practices in data pre-processing, hyper-parameter tuning, and model evaluation; tools/libraries/APIs such as scikit-learn, Theano/Keras, and multi/many-core CPU/GPU programming.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
This course introduces algorithms, tools, practices, and applications of machine learning. Topics include core methods such as supervised learning (classification and regression), unsupervised learning (clustering, principal component analysis), Bayesian estimation, neural networks; common practices in data pre-processing, hyper-parameter tuning, and model evaluation; tools/libraries/APIs such as scikit-learn, Theano/Keras, and multi/many-core CPU/GPU programming.
On successful completion of the course, students should be able to:
[1] understand the motivations and principles for building adaptive systems based on empirical data, and how machine learning relates to the broader field of artificial intelligence
[2] formulate problems associated with domain specific data (e.g., image classification, document clustering) in terms of abstract models of machine learning
[3] implement solutions to machine learning problems using tools such as Matlab or Octave, apply numerical optimization algorithms"""
)

course17 = Course(
    course_id="034494",
    course_name="COMP3316",
    teacher=Teacher.objects.get(name="Dr. Giulio Chiribella"),
    description="Quantum information and computation",
    course_information = """Pass in MATH1853 or MATH2014 or MATH2101 or equivalent (e.g. PHYS2155)

Approved Syllabus
This course offers an introduction to the interdisciplinary field of quantum information and computation. We will start from the basic rules of quantum theory and become familiar with the counterintuitive notions of quantum superposition and entanglement. In particular, we will see how quantum systems could be used to detect an object without directly interacting with it (Elitzur-Vaidman bomb tester), to increase the amount of bits that can be sent through a transmission line (dense coding), and to increase the chance to win certain games (CHSH game and GHZ game). Once the basics have been covered, we will provide an overview of quantum computation and of major quantum algorithms such as Grover's search algorithm and Shor's factoring algorithm for prime factorization. Finally, we will introduce the upgraded framework of quantum theory, and use it to explore applications to quantum error correction, quantum state discrimination, quantum cryptography, and quantum teleportation.
Assessment: 50% continuous assignment, 50% examination

Course Objectives
This course offers an introduction to the interdisciplinary field of quantum information and computation. We will start from the basic rules of quantum theory and become familiar with the counterintuitive notions of quantum superposition and entanglement. In particular, we will see how quantum systems could be used to detect an object without directly interacting with it (Elitzur-Vaidman bomb tester), to increase the amount of bits that can be sent through a transmission line (dense coding), and to increase the chance to win certain games (CHSH game and GHZ game). Once the basics have been covered, we will provide an overview of quantum computation and of major quantum algorithms such as Grover's search algorithm and Shor's factoring algorithm for prime factorization. Finally, we will introduce the upgraded framework of quantum theory, and use it to explore applications to quantum error correction, quantum state discrimination, quantum cryptography, and quantum teleportation. 
On successful completion of the course, students should be able to:
[Basic Working knowledge]
Able to use the basic rules of quantum theory: states, measurements, gates, composite systems.
[Modeling] Able to model basic information-theoretic tasks in the quantum domain: quantum communication, quantum games, quantum computation.
[Higher-level reasoning]  Able to deduce new results from the basic knowledge provided in the course.
[Self-learning] Able to self-learn a new topic and/or to approach a mini research problem."""
)

course18 = Course(
    course_id="030837",
    course_name="COMP3322",
    teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"),
    description="Modern Technologies on World Wide Web",
    course_information = """Pass in COMP1117 or ENGG1330; Mutually exclusive with: IIMT3663

Approved Syllabus
Selected network protocols relevant to the World Wide Web (e.g., HTTP, DNS, IP); World Wide Web; technologies for programming the Web (e.g, HTML, XML, style sheets, PHP, JavaScript, Node.js.; other topics of current interest (AJAX, HTML5, web services, cloud computing).
Assessment: 60% continuous assessment, 40% examination

Course Objectives
Selected network protocols relevant to the World Wide Web (e.g., HTTP, DNS, IP); World Wide Web; technologies for programming the Web (e.g, HTML, style sheets, PHP, JavaScript, Node.js.; other topics of current interest (AJAX, HTML5, web services, cloud computing).
On successful completion of the course, students should be able to:
[Web technologies]
Able to master the key technologies about the World Wide Web and be able to contrast similar technologies.
[Application Development]
Able to implement web based systems to solving real-life problems """
)

course19 = Course(
    course_id="030838",
    course_name="COMP3323",
    teacher=Teacher.objects.get(name="Dr. R.C.K. Cheng"),
    description="Advanced database systems",
    course_information = """Pass in COMP3278; Mutually exclusive with: FITE3010

Approved Syllabus
The course will study some advanced topics and techniques in database systems, with a focus on the system and algorithmic aspects.  It will also survey the recent development and progress in selected areas.  Topics include: query optimization, spatial-spatiotemporal data management, multimedia and time-series data management, information retrieval and XML, data mining.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
The course will study some advanced topics and techniques in database systems, with a focus on the system and algorithmic aspects. It will also survey the recent development and progress in selected areas. Topics include: query optimization, spatial-spatiotemporal data management, multimedia and time-series data management, information retrieval and XML, data mining.
On successful completion of the course, students should be able to:
[Advanced Topics in Databases] Able to understand the background and knowledge of some advanced topics in database that have become key techniques in modern database theory and practices; typical topics are distributed concurrency control, database recovery, query optimization, spatial databases.
[Recent Development in Database Research] Able to understand the background and knowledge of some contemporary topics in database research; typical topics are data mining, uncertain data management, XML data.
[Recent Development in Information Management] Able to understand the background and knowledge of some contemporary topics in information management, typical topics are cloud computing, web information management, social network technology.
[Application Development] Able to implement some practical application modules based on selected advanced database techniques. """
)

    
course20 = Course(
    course_id="030844",
    course_name="COMP3329",
    teacher=Teacher.objects.get(name="Dr. T.W. Chim"),
    description="Computer game design and programming",
    course_information = """Pass in ENGG1340 or COMP2113 or COMP2123

Approved Syllabus
To study the principles and practice of computer game design.
This course introduces the concepts and techniques for computer game design and development. Topics include: game history and genres, game design process, game engine, audio and visual design, 2D and 3D graphics, physics, optimization, camera, network, artificial intelligence and user interface design. Students participate in group projects to gain hands-on experience in using common game engine in the market.
Assessment: 50% continuous assessment, 50% examination

Course Objectives
On successful completion of the course, students should be able to:
[implement a workable game in particular platform]
Be able to implement a workable game in particular platform
[understand different aspects of game design]
Be able to understand different aspects of game design including UI, programming, marketing, etc.
[present the game idea in both written and oral form]
Be able to present the game idea in both written and oral form
[learn new development environment]
Be able to learn new development environment 
[learn from other source codes and projects]
Be able to learn from other source codes and projects """
)
    


for i in range(1,21):
    #print(i)
    name = f"course{i}"
    #print(name,globals()[name])
    course = globals()[name]
    course.save()
    #course, created = Course.objects.get_or_create(globals()[name])
   # if not created:
    #    break

