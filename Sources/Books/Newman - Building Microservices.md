---
kindle-bookId: '19220'
kindle-title: 'Building Microservices: Designing Fine-Grained Systems'
kindle-author: Sam Newman
kindle-highlightsCount: 590
kindle-asin: B09B5L4NVT
kindle-lastAnnotatedDate: '2025-11-15'
kindle-bookImageUrl: 'https://m.media-amazon.com/images/I/81dmHMoJDjL._SX1024.jpg'
---
# Building Microservices
## Metadata
* Author: [Sam Newman](https://amazon.com//Sam-Newman/e/B00LEP6IB0/ref=aufs_dp_fta_an_dsk)
* ASIN: B09B5L4NVT
* Reference: https://amazon.com/dp/B09B5L4NVT
* [Kindle link](kindle://book?action=open&asin=B09B5L4NVT)

## Highlights
They are a type of service-oriented architecture, albeit one that is opinionated about how service boundaries should be drawn, and one in which independent deployability is key. They are technology agnostic, which is one of the advantages they offer. — location: [213](kindle://book?action=open&asin=B09B5L4NVT&location=213) ^ref-63351

---
Microservices embrace the concept of information hiding.1 Information hiding means hiding as much information as possible inside a component and exposing as little as possible via external interfaces. This allows for clear separation between what can change easily and what is more difficult to change. — location: [223](kindle://book?action=open&asin=B09B5L4NVT&location=223) ^ref-1473

---
Implementation that is hidden from external parties can be changed freely as long as the networked interfaces the microservice exposes don’t change in a backward-incompatible fashion. — location: [226](kindle://book?action=open&asin=B09B5L4NVT&location=226) ^ref-2120

---
Changes inside a microservice boundary (as shown in Figure 1-1) shouldn’t affect an upstream consumer, enabling independent releasability of functionality. — location: [228](kindle://book?action=open&asin=B09B5L4NVT&location=228) ^ref-3504

---
Having clear, stable service boundaries that don’t change when the internal implementation changes results in systems that have looser coupling and stronger cohesion. — location: [230](kindle://book?action=open&asin=B09B5L4NVT&location=230) ^ref-18326

---
SOA at its heart is a sensible idea. However, despite many efforts, there is a lack of good consensus on how to do SOA well. In my opinion, much of the industry failed to look holistically enough at the problem and present a compelling alternative to the narrative set out by various vendors in this space. — location: [247](kindle://book?action=open&asin=B09B5L4NVT&location=247) ^ref-18380

---
The microservice approach has emerged from real-world use, taking our better understanding of systems and architecture to do SOA well. You should think of microservices as being a specific approach for SOA in the same way that Extreme Programming (XP) or Scrum is a specific approach for Agile software development. — location: [254](kindle://book?action=open&asin=B09B5L4NVT&location=254) ^ref-1251

---
If you take only one thing from this book and from the concept of microservices in general, it should be this: ensure that you embrace the concept of independent deployability of your microservices. Get into the habit of deploying and releasing changes to a single microservice into production without having to deploy anything else. From this, many good things will follow. — location: [267](kindle://book?action=open&asin=B09B5L4NVT&location=267) ^ref-34040

---
To ensure independent deployability, we need to make sure our microservices are loosely coupled: we must be able to change one service without having to change anything else. This means we need explicit, well-defined, and stable contracts between services. — location: [270](kindle://book?action=open&asin=B09B5L4NVT&location=270) ^ref-35569

---
By modeling services around business domains, we can make it easier to roll out new functionality and to recombine microservices in different ways to deliver new functionality to our users. — location: [282](kindle://book?action=open&asin=B09B5L4NVT&location=282) ^ref-12830

---
By making our services end-to-end slices of business functionality, we ensure that our architecture is arranged to make changes to business functionality as efficient as possible. Arguably, with microservices we have made a decision to prioritize high cohesion of business functionality over high cohesion of technical functionality. — location: [292](kindle://book?action=open&asin=B09B5L4NVT&location=292) ^ref-6015

---
Hiding internal state in a microservice is analogous to the practice of encapsulation in object-oriented (OO) programming. Encapsulation of data in OO systems is an example of information hiding in action. — location: [307](kindle://book?action=open&asin=B09B5L4NVT&location=307) ^ref-42030

---
I urge people not to worry about size. When you are first starting out, it’s much more important that you focus on two key things. First, how many microservices can you handle? As you have more services, the complexity of your system will increase, and you’ll need to learn new skills (and perhaps adopt new technology) to cope with this. — location: [336](kindle://book?action=open&asin=B09B5L4NVT&location=336) ^ref-60810

---
A move to microservices will introduce new sources of complexity, with all the challenges this can bring. It’s for this reason that I am a strong advocate for incremental migration to a microservice architecture. — location: [338](kindle://book?action=open&asin=B09B5L4NVT&location=338) ^ref-40355

---
Second, how do you define microservice boundaries to get the most out of them, without everything becoming a horribly coupled mess? These topics are much more important to focus on when you start your journey. — location: [340](kindle://book?action=open&asin=B09B5L4NVT&location=340) ^ref-29463

---
We don’t know what the future holds, so we’d like an architecture that can theoretically help us solve whatever problems we might face down the road. — location: [346](kindle://book?action=open&asin=B09B5L4NVT&location=346) ^ref-17216

---
Finding a balance between keeping your options open and bearing the cost of architectures like this can be a real art. — location: [347](kindle://book?action=open&asin=B09B5L4NVT&location=347) ^ref-57899

---
As you turn up the dial, and you have more microservices, you have increased flexibility. — location: [349](kindle://book?action=open&asin=B09B5L4NVT&location=349) ^ref-21977

---
But you likely ramp up the pain points too. This is yet another reason I strongly advocate incremental adoption of microservices. — location: [349](kindle://book?action=open&asin=B09B5L4NVT&location=349) ^ref-20351

---
The now famous Conway’s law states the following: Organizations which design systems...are constrained to produce designs which are copies of the communication structures of these organizations. Melvin Conway, “How Do Committees Invent?” The three-tiered architecture is a good example of this law in action. In the past, the primary way IT organizations grouped people was in terms of their core competency: — location: [368](kindle://book?action=open&asin=B09B5L4NVT&location=368) ^ref-8054

---
That explains why this architecture is so common. It’s not bad; it’s just optimized around one set of forces—how we traditionally grouped people, around familiarity. But the forces have changed. Our aspirations around our software have changed. We now group people in poly-skilled teams to reduce handoffs and silos. — location: [376](kindle://book?action=open&asin=B09B5L4NVT&location=376) ^ref-16240

---
If we want to make it easier to make changes, instead we need to change how we group code, choosing cohesion of business functionality rather than technology. Each service may or may not end up containing a mix of these three layers, but that is a local service implementation concern. — location: [382](kindle://book?action=open&asin=B09B5L4NVT&location=382) ^ref-25682

---
In such a situation, our Customer microservice encapsulates a thin slice of each of the three tiers—it has a bit of UI, a bit of application logic, and a bit of data storage. Our business domain becomes the primary force driving our system architecture, hopefully making it easier to make changes, as well as making it easier for us to align our teams to lines of business within the organization. — location: [401](kindle://book?action=open&asin=B09B5L4NVT&location=401) ^ref-17113

---
Often, the UI is not provided directly by the microservice, but even if this is the case, we would expect the portion of the UI related to this functionality to still be owned by the Customer Profile Team, — location: [404](kindle://book?action=open&asin=B09B5L4NVT&location=404) ^ref-13578

---
This concept of a team owning an end-to-end slice of user-facing functionality is gaining traction. The book Team Topologies4 introduces the idea of a stream-aligned team, which embodies this concept: — location: [407](kindle://book?action=open&asin=B09B5L4NVT&location=407) ^ref-9586

---
A stream-aligned team is a team aligned to a single, valuable stream of work...[T]he team is empowered to build and deliver customer or user value as quickly, safely, and independently as possible, without requiring hand-offs to other teams to perform parts of the work. — location: [410](kindle://book?action=open&asin=B09B5L4NVT&location=410) ^ref-39366

---
A classic single-process monolithic deployment can make sense for many organizations. — location: [444](kindle://book?action=open&asin=B09B5L4NVT&location=444) ^ref-17256

---
Even as the organization grows, however, the monolith can potentially grow with it, which brings us to the modular monolith. — location: [447](kindle://book?action=open&asin=B09B5L4NVT&location=447) ^ref-33078

---
The concept of breaking software into modules is nothing new; modular software has its roots in work done around structured programming in the 1970s, and even further back than that. Nonetheless, this is an approach that I still don’t see enough organizations properly engage with. — location: [453](kindle://book?action=open&asin=B09B5L4NVT&location=453) ^ref-61339

---
For many organizations, the modular monolith can be an excellent choice. If the module boundaries are well defined, it can allow for a high degree of parallel work, while avoiding the challenges of the more distributed microservice architecture by having a much simpler deployment topology. — location: [457](kindle://book?action=open&asin=B09B5L4NVT&location=457) ^ref-36484

---
I have seen some teams attempt to push the idea of the modular monolith further by having the database decomposed along the same lines as the modules, — location: [463](kindle://book?action=open&asin=B09B5L4NVT&location=463) ^ref-36901

---
In my experience, a distributed monolith has all the disadvantages of a distributed system, and the disadvantages of a single-process monolith, without having enough of the upsides of either. — location: [475](kindle://book?action=open&asin=B09B5L4NVT&location=475) ^ref-45309

---
Distributed monoliths typically emerge in an environment in which not enough focus was placed on concepts like information hiding and cohesion of business functionality. Instead, highly coupled architectures cause changes to ripple across service boundaries, and seemingly innocent changes that appear to be local in scope break other parts of the system. — location: [478](kindle://book?action=open&asin=B09B5L4NVT&location=478) ^ref-53387

---
A multitude of studies have shown the challenges of confused lines of ownership.8 I refer to this problem as delivery contention. — location: [485](kindle://book?action=open&asin=B09B5L4NVT&location=485) ^ref-48894

---
But a microservice architecture does give you more concrete boundaries around which ownership lines can be drawn in a system, giving you much more flexibility when it comes to reducing this problem. — location: [489](kindle://book?action=open&asin=B09B5L4NVT&location=489) ^ref-48916

---
Advantages of Monoliths Some monoliths, such as the single-process or modular monoliths, have a whole host of advantages too. Their much simpler deployment topology can avoid many of the pitfalls associated with distributed systems. This can result in much simpler developer workflows, and monitoring, troubleshooting, and activities like end-to-end testing can be greatly simplified as well. — location: [491](kindle://book?action=open&asin=B09B5L4NVT&location=491) ^ref-10757

---
Monoliths can also simplify code reuse within the monolith itself. If we want to reuse code within a distributed system, we need to decide whether we want to copy code, break out libraries, or push the shared functionality into a service. With a monolith, our choices are much simpler, and many people like that simplicity—all the code is there; just use it! — location: [495](kindle://book?action=open&asin=B09B5L4NVT&location=495) ^ref-54982

---
Unfortunately, people have come to view the monolith as something to be avoided—as something inherently problematic. I’ve met multiple people for whom the term monolith is synonymous with legacy. — location: [498](kindle://book?action=open&asin=B09B5L4NVT&location=498) ^ref-56058

---
A monolithic architecture is a choice, and a valid one at that. I’d go further and say that in my opinion it is the sensible default choice as an architectural style. In other words, I am looking for a reason to be convinced to use microservices, rather than looking for a reason not to use them. — location: [501](kindle://book?action=open&asin=B09B5L4NVT&location=501) ^ref-61828

---
If we fall into the trap of systematically undermining the monolith as a viable option for delivering our software, we’re at risk of not doing right by ourselves or by the users of our software. — location: [503](kindle://book?action=open&asin=B09B5L4NVT&location=503) ^ref-25474

---
As I touched on earlier, I don’t think you need to adopt lots of new technology when you first start using microservices. In fact, that can be counterproductive. Instead, as you ramp up your microservice architecture, you should constantly be looking for issues caused by your increasingly distributed system, and then for technology that might help. — location: [507](kindle://book?action=open&asin=B09B5L4NVT&location=507) ^ref-62227

---
technology has played a large part in the adoption of microservices as a concept. Understanding the tools that are available to help you get the most out of this architecture is going to be a key part of making any implementation of microservices a success. — location: [510](kindle://book?action=open&asin=B09B5L4NVT&location=510) ^ref-25575

---
In fact, I would go as far to say that microservices require an understanding of the supporting technology to such a degree that previous distinctions between logical and physical architecture can be problematic—if you are involved in helping shape a microservice architecture, you’ll need a breadth of understanding of these two worlds. — location: [512](kindle://book?action=open&asin=B09B5L4NVT&location=512) ^ref-25188

---
Be cautious about taking on too much new technology when you start off with microservices. That said, a log aggregation tool is so essential that you should consider it a prerequisite for adopting microservices. — location: [523](kindle://book?action=open&asin=B09B5L4NVT&location=523) ^ref-44808

---
You can make these log aggregation tools even more useful by implementing correlation IDs, in which a single ID is used for a related set of service calls—for example, the chain of calls that might be triggered due to user interaction. By logging this ID as part of each log entry, isolating the logs associated with a given flow of calls becomes much easier, which in turn makes troubleshooting much easier. — location: [528](kindle://book?action=open&asin=B09B5L4NVT&location=528) ^ref-20739

---
Virtualization is one way to create isolated execution environments on existing hardware, but normal virtualization techniques can be quite heavy when we consider the size of our microservices. — location: [548](kindle://book?action=open&asin=B09B5L4NVT&location=548) ^ref-33935

---
Containers, on the other hand, provide a much more lightweight way to provision isolated execution for service instances, resulting in faster spin-up times for new container instances, along with being much more cost effective for many architectures. — location: [549](kindle://book?action=open&asin=B09B5L4NVT&location=549) ^ref-19901

---
Don’t feel the need to rush to adopt Kubernetes, or even containers for that matter. They absolutely offer significant advantages over more traditional deployment techniques, but their adoption is difficult to justify if you have only a few microservices. After the overhead of managing deployment begins to become a significant headache, start considering containerization of your service and the use of Kubernetes. — location: [555](kindle://book?action=open&asin=B09B5L4NVT&location=555) ^ref-10383

---
But if you do end up doing that, do your best to ensure that someone else is running the Kubernetes cluster for you, perhaps by making use of a managed service on a public cloud provider. Running your own Kubernetes cluster can be a significant amount of work! — location: [558](kindle://book?action=open&asin=B09B5L4NVT&location=558) ^ref-51543

---
For many people, Apache Kafka has become the de facto choice for streaming data in a microservice environment, and for good reason. — location: [566](kindle://book?action=open&asin=B09B5L4NVT&location=566) ^ref-13485

---
Microservices, however, tend to achieve these benefits to a greater degree primarily because they take a more opinionated stance in the way service boundaries are defined. By combining the concepts of information hiding and domain-driven design with the power of distributed systems, microservices can help deliver significant gains over other forms of distributed architectures. — location: [592](kindle://book?action=open&asin=B09B5L4NVT&location=592) ^ref-44102

---
With a system composed of multiple, collaborating microservices, we can decide to use different technologies inside each one. This allows us to pick the right tool for each job rather than having to select a more standardized, one-size-fits-all approach that often ends up being the lowest common denominator. — location: [596](kindle://book?action=open&asin=B09B5L4NVT&location=596) ^ref-9804

---
A key concept in improving the robustness of your application is the bulkhead. A component of a system may fail, but as long as that failure doesn’t cascade, you can isolate the problem, and the rest of the system can carry on working. Service boundaries become your obvious bulkheads. — location: [621](kindle://book?action=open&asin=B09B5L4NVT&location=621) ^ref-39497

---
Networks can and will fail, as will machines. We need to know how to handle such failures and the impact (if any) those failures will have on the end users of our software. I have certainly worked with teams who have ended up with a less robust system after their migration to microservices due to their not taking these concerns seriously enough. — location: [627](kindle://book?action=open&asin=B09B5L4NVT&location=627) ^ref-3948

---
A one-line change to a million-line monolithic application requires the entire application to be deployed in order to release the change. That could be a large-impact, high-risk deployment. In practice, deployments such as these end up happening infrequently because of understandable fear. Unfortunately, this means that our changes continue to build up between releases, until the new version of our application entering production has masses of changes. And the bigger the delta between releases, the higher the risk that we’ll get something wrong! — location: [648](kindle://book?action=open&asin=B09B5L4NVT&location=648) ^ref-27053

---
Microservices allow us to better align our architecture to our organization, helping us minimize the number of people working on any one codebase to hit the sweet spot of team size and productivity. — location: [661](kindle://book?action=open&asin=B09B5L4NVT&location=661) ^ref-60718

---
Microservices also allow us to change ownership of services as the organization changes—enabling us to maintain the alignment between architecture and organization in the future. — location: [662](kindle://book?action=open&asin=B09B5L4NVT&location=662) ^ref-13893

---
Now we need to think of the myriad ways that we might want to weave together capabilities for the web, native application, mobile web, tablet app, or wearable device. As organizations move away from thinking in terms of narrow channels to embracing more holistic concepts of customer engagement, we need architectures that can keep up. — location: [668](kindle://book?action=open&asin=B09B5L4NVT&location=668) ^ref-36217

---
the bulk of this book is about dealing with the pain, suffering, and horror of owning a microservice architecture. — location: [680](kindle://book?action=open&asin=B09B5L4NVT&location=680) ^ref-20724

---
Developer Experience As you have more and more services, the developer experience can begin to suffer. More resource-intensive runtimes like the JVM can limit the number of microservices that can be run on a single developer machine. I could probably run four or five JVM-based microservices as separate processes on my laptop, but could I run 10 or 20? Most likely not. Even with less taxing runtimes, there is a limit to the number of things you can run locally, which inevitably will start conversations about what to do when you can’t run the entire system on one machine. This can become even more complicated if you are using cloud services that you cannot run locally. — location: [682](kindle://book?action=open&asin=B09B5L4NVT&location=682) ^ref-11181

---
Extreme solutions can involve “developing in the cloud,” where developers move away from being able to develop locally anymore. I’m not a fan of this, because feedback cycles can suffer greatly. — location: [688](kindle://book?action=open&asin=B09B5L4NVT&location=688) ^ref-56185

---
I think limiting the scope of which parts of a system a developer needs to work on is likely to be a much more straightforward approach. However, this might be problematic if you want to embrace more of a “collective ownership” model in which any developer is expected to work on any part of the system. — location: [689](kindle://book?action=open&asin=B09B5L4NVT&location=689) ^ref-56414

---
some advances have legitimately helped in dealing with the complexity of these sorts of architectures. There is a danger, though, that this wealth of new toys can lead to a form of technology fetishism. — location: [695](kindle://book?action=open&asin=B09B5L4NVT&location=695) ^ref-47471

---
Microservices may well give you the option for each microservice to be written in a different programming language, to run on a different runtime, or to use a different database—but these are options, not requirements. You have to carefully balance the breadth and complexity of the technology you use against the costs that a diverse array of technology can bring. — location: [698](kindle://book?action=open&asin=B09B5L4NVT&location=698) ^ref-38923

---
When you start adopting microservices, some fundamental challenges are inescapable: you’ll need to spend a lot of time understanding issues around data consistency, latency, service modeling, and the like. If you’re trying to understand how these ideas change the way you think about software development at the same time that you’re embracing a huge amount of new technology, you’ll have a hard time of it. It’s also worth pointing out that the bandwidth taken up by trying to understand all of this new technology will reduce the time you have for actually shipping features to your users. — location: [701](kindle://book?action=open&asin=B09B5L4NVT&location=701) ^ref-25985

---
As you (gradually) increase the complexity of your microservice architecture, look to introduce new technology as you need it. You don’t need a Kubernetes cluster when you have three services! In addition to ensuring that you’re not overloaded with the complexity of these new tools, this gradual increase has the added benefit of allowing you to gain new and better ways of doing things that will no doubt emerge over time. — location: [705](kindle://book?action=open&asin=B09B5L4NVT&location=705) ^ref-33607

---
In my experience, microservices are a poor choice for an organization primarily concerned with reducing costs, as a cost-cutting mentality—where IT is seen as a cost center rather than a profit center—will constantly be a drag on getting the most out of this architecture. — location: [714](kindle://book?action=open&asin=B09B5L4NVT&location=714) ^ref-29020

---
On the other hand, microservices can help you make more money if you can use these architectures to reach more customers or develop more functionality in parallel. — location: [716](kindle://book?action=open&asin=B09B5L4NVT&location=716) ^ref-63688

---
So are microservices a way to drive more profits? Perhaps. Are microservices a way to reduce costs? Not so much. — location: [717](kindle://book?action=open&asin=B09B5L4NVT&location=717) ^ref-19750

---
With a microservice architecture, we have broken up this monolithic schema. That doesn’t mean that the need for reporting across all our data has gone away; we’ve just made it much more difficult, because now our data is scattered across multiple logically isolated schemas. — location: [725](kindle://book?action=open&asin=B09B5L4NVT&location=725) ^ref-10152

---
But with a microservice architecture, the scope of our end-to-end tests becomes very large. We would now need to run tests across multiple processes, all of which need to be deployed and appropriately configured for the test scenarios. We also need to be prepared for the false negatives that occur when environmental issues, such as service instances dying or network time-outs of failed deployments, cause our tests to fail. — location: [757](kindle://book?action=open&asin=B09B5L4NVT&location=757) ^ref-9679

---
These forces mean that as your microservice architecture grows, you will get a diminishing return on investment when it comes to end-to-end testing. The testing will cost more but won’t manage to give you the same level of confidence that it did in the past. — location: [760](kindle://book?action=open&asin=B09B5L4NVT&location=760) ^ref-1715

---
Information that previously flowed within only a single process now needs to be serialized, transmitted, and deserialized over networks that you might be exercising more than ever before. All of this can result in worsening latency of your system. — location: [767](kindle://book?action=open&asin=B09B5L4NVT&location=767) ^ref-33967

---
Make a small change and then measure the impact. This assumes that you have some way of measuring the end-to-end latency for the operations you care about—distributed — location: [770](kindle://book?action=open&asin=B09B5L4NVT&location=770) ^ref-12322

---
Sometimes making an operation slower is perfectly acceptable, as long as it is still fast enough! — location: [773](kindle://book?action=open&asin=B09B5L4NVT&location=773) ^ref-23796

---
Whereas in the past you might have relied on database transactions to manage state changes, you’ll need to understand that similar safety cannot easily be provided in a distributed system. The use of distributed transactions in most cases proves to be highly problematic in coordinating state changes. — location: [777](kindle://book?action=open&asin=B09B5L4NVT&location=777) ^ref-1078

---
Adopting an incremental approach to decomposition, so that you are able to assess the impact of changes to your architecture in production, is really important. — location: [783](kindle://book?action=open&asin=B09B5L4NVT&location=783) ^ref-42458

---
Given the importance of defining stable service boundaries, I feel that microservice architectures are often a bad choice for brand-new products or startups. In either case, the domain that you are working with is typically undergoing significant change as you iterate on the fundamentals of what you are trying to build. This shift in domain models will, in turn, result in more changes being made to service boundaries, and coordinating changes across service boundaries is an expensive undertaking. In general, I feel it’s more appropriate to wait until enough of the domain model has stabilized before looking to define service boundaries. — location: [794](kindle://book?action=open&asin=B09B5L4NVT&location=794) ^ref-29687

---
I do see a temptation for startups to go microservice first, the reasoning being, “If we’re really successful, we’ll need to scale!” The problem is that you don’t necessarily know if anyone is even going to want to use your new product. And even if you do become successful enough to require a highly scalable architecture, the thing you end up delivering to your users might be very different from what you started building in the first place. — location: [798](kindle://book?action=open&asin=B09B5L4NVT&location=798) ^ref-54910

---
Startups also typically have fewer people available to build the system, which creates more challenges with respect to microservices. Microservices bring with them sources of new work and complexity, and this can tie up valuable bandwidth. The smaller the team, the more pronounced this cost will be. When working with smaller teams with just a handful of developers, I’m very hesitant to suggest microservices for this reason. — location: [803](kindle://book?action=open&asin=B09B5L4NVT&location=803) ^ref-53239

---
Some people have described this as the “microservice tax.” When that investment benefits lots of people, it’s easier to justify. But if one person out of your five-person team is spending their time on these issues, that’s a lot of valuable time not being spent building your product. — location: [808](kindle://book?action=open&asin=B09B5L4NVT&location=808) ^ref-39288

---
It’s much easier to move to microservices later, after you understand where the constraints are in your architecture and what your pain points are—then you can focus your energy on using microservices in the most sensible places. — location: [810](kindle://book?action=open&asin=B09B5L4NVT&location=810) ^ref-54108

---
In my experience, probably the single biggest reason that organizations adopt microservices is to allow for more developers to work on the same system without getting in each other’s way. Get your architecture and organizational boundaries right, and you allow more people to work independently of each other, reducing delivery contention. — location: [819](kindle://book?action=open&asin=B09B5L4NVT&location=819) ^ref-1342

---
Software as a Service (SaaS) applications are, in general, also a good fit for a microservice architecture. These products are typically expected to operate 24-7, which creates challenges when it comes to rolling out changes. — location: [823](kindle://book?action=open&asin=B09B5L4NVT&location=823) ^ref-57073

---
However, I still think that they are an architectural choice whose use must be justified by the problems you are trying to solve; often, simpler approaches can deliver much more easily. — location: [845](kindle://book?action=open&asin=B09B5L4NVT&location=845) ^ref-48006

---
When the core concepts of microservices are properly understood and implemented, they can help create empowering, productive architectures that can help systems become more than the sum of their parts. — location: [847](kindle://book?action=open&asin=B09B5L4NVT&location=847) ^ref-31649

---
In this chapter, we’ll look at some foundational concepts such as information hiding, coupling, and cohesion and understand how they’ll shift our thinking about drawing boundaries around our microservices. — location: [878](kindle://book?action=open&asin=B09B5L4NVT&location=878) ^ref-55930

---
In essence, microservices are just another form of modular decomposition, albeit one that has network-based interaction between the models and all the associated challenges that brings. — location: [900](kindle://book?action=open&asin=B09B5L4NVT&location=900) ^ref-14669

---
The connections between modules are the assumptions which the modules make about each other. By reducing the number of assumptions that one module (or microservice) makes about another, we directly impact the connections between them. By keeping the number of assumptions small, it is easier to ensure that we can change one module without impacting others. — location: [924](kindle://book?action=open&asin=B09B5L4NVT&location=924) ^ref-21204

---
One of the most succinct definitions I’ve heard for describing cohesion is this: “the code that changes together, stays together.”4 For our purposes, this is a pretty good definition. — location: [933](kindle://book?action=open&asin=B09B5L4NVT&location=933) ^ref-33653

---
We want related behavior to sit together, and unrelated behavior to sit elsewhere. Why? Well, if we want to change behavior, we want to be able to change it in one place, and to release that change as soon as possible. If we have to change that behavior in lots of different places, we’ll have to release lots of different services (perhaps at the same time) to deliver that change. — location: [938](kindle://book?action=open&asin=B09B5L4NVT&location=938) ^ref-36852

---
Making changes in lots of different places is slower, and deploying lots of services at once is risky—thus we want to avoid both. — location: [940](kindle://book?action=open&asin=B09B5L4NVT&location=940) ^ref-57892

---
If the related functionality is spread across the system, we say that cohesion is weak—whereas for our microservice architectures we’re aiming for strong cohesion. — location: [943](kindle://book?action=open&asin=B09B5L4NVT&location=943) ^ref-11992

---
What sorts of things cause tight coupling? A classic mistake is to pick an integration style that tightly binds one service to another, causing changes inside the service to require a change to consumers. — location: [949](kindle://book?action=open&asin=B09B5L4NVT&location=949) ^ref-50121

---
A loosely coupled service knows as little as it needs to about the services with which it collaborates. This also means we probably want to limit the number of different types of calls from one service to another, because beyond the potential performance problem, chatty communication can lead to tight coupling. — location: [951](kindle://book?action=open&asin=B09B5L4NVT&location=951) ^ref-4094

---
A structure is stable if cohesion is strong and coupling is low.5 — location: [961](kindle://book?action=open&asin=B09B5L4NVT&location=961) ^ref-62181

---
The concept here of stability is important to us. For our microservice boundaries to deliver on the promise of independent deployability, allowing us to work on microservices in parallel and reduce the amount of coordination between teams working on these services, we need some degree of stability in the boundaries themselves. If the contract that a microservice exposes is constantly changing in a backward-incompatible fashion, then this will cause upstream consumers to constantly have to change too. — location: [963](kindle://book?action=open&asin=B09B5L4NVT&location=963) ^ref-36677

---
Cohesion applies to the relationship between things inside a boundary (a microservice in our context), whereas coupling describes the relationship between things across a boundary. — location: [968](kindle://book?action=open&asin=B09B5L4NVT&location=968) ^ref-49118

---
Sometimes parts of your system may be going through so much change that stability might be impossible. — location: [973](kindle://book?action=open&asin=B09B5L4NVT&location=973) ^ref-64594

---
Ultimately, some coupling in our system will be unavoidable. What we want to do is reduce how much coupling we have. — location: [979](kindle://book?action=open&asin=B09B5L4NVT&location=979) ^ref-60828

---
Just remember the importance of information hiding. Share only what you absolutely have to, and send only the absolute minimum amount of data that you need. — location: [1027](kindle://book?action=open&asin=B09B5L4NVT&location=1027) ^ref-2800

---
Temporal coupling has a subtly different meaning in the context of a distributed system, where it refers to a situation in which one microservice needs another microservice to do something at the same time for the operation to complete. — location: [1033](kindle://book?action=open&asin=B09B5L4NVT&location=1033) ^ref-50961

---
Temporal coupling isn’t always bad; it’s just something to be aware of. As you have more microservices, with more complex interactions between them, the challenges of temporal coupling can increase to such a point that it becomes more difficult to scale your system and keep it working. — location: [1046](kindle://book?action=open&asin=B09B5L4NVT&location=1046) ^ref-48980

---
One of the ways to avoid temporal coupling is to use some form of asynchronous communication, such as a message broker. — location: [1048](kindle://book?action=open&asin=B09B5L4NVT&location=1048) ^ref-16410

---
At least by hiding this detail we could much more easily phase deployment. — location: [1108](kindle://book?action=open&asin=B09B5L4NVT&location=1108) ^ref-52316

---
Common Coupling Common coupling occurs when two or more microservices make use of a common set of data. A simple and common example of this form of coupling would be multiple microservices making use of the same shared database, but it could also manifest itself in the use of shared memory or a shared filesystem. — location: [1121](kindle://book?action=open&asin=B09B5L4NVT&location=1121) ^ref-21191

---
Common coupling becomes more problematic, though, if the structure of the common data changes more frequently, or if multiple microservices are reading and writing to the same data. — location: [1135](kindle://book?action=open&asin=B09B5L4NVT&location=1135) ^ref-41549

---
Conceptually, we have both the Order Processor and Warehouse microservices managing different aspects of the life cycle of an order. — location: [1149](kindle://book?action=open&asin=B09B5L4NVT&location=1149) ^ref-51294

---
One way to ensure that the state of something is changed in a correct fashion would be to create a finite state machine. A state machine can be used to manage the transition of some entity from one state to another, ensuring invalid state transitions are prohibited. — location: [1153](kindle://book?action=open&asin=B09B5L4NVT&location=1153) ^ref-30395

---
In this situation, it is really important that we see the requests from Warehouse and Order Processor as just that—requests. — location: [1170](kindle://book?action=open&asin=B09B5L4NVT&location=1170) ^ref-19059

---
Tip Make sure you see a request that is sent to a microservice as something that the downstream microservice can reject if it is invalid. — location: [1176](kindle://book?action=open&asin=B09B5L4NVT&location=1176) ^ref-30373

---
If you see a microservice that just looks like a thin wrapper around database CRUD operations, that is a sign that you may have weak cohesion and tighter coupling, as logic that should be in that service to manage the data is instead spread elsewhere in your system. — location: [1182](kindle://book?action=open&asin=B09B5L4NVT&location=1182) ^ref-64419

---
Sources of common coupling are also potential sources of resource contention. Multiple microservices making use of the same filesystem or database could overload that shared resource, potentially causing significant problems if the shared resource becomes slow or even entirely unavailable. A shared database is especially prone to this problem, as multiple consumers can run arbitrary queries against the database itself, which in turn can have wildly different performance characteristics. — location: [1187](kindle://book?action=open&asin=B09B5L4NVT&location=1187) ^ref-33901

---
I’ve seen more than one database brought to its knees by an expensive SQL query—I may have even been the culprit once or twice. — location: [1191](kindle://book?action=open&asin=B09B5L4NVT&location=1191) ^ref-64193

---
Content coupling describes a situation in which an upstream service reaches into the internals of a downstream service and changes its internal state. The most common manifestation of this is an external service accessing another microservice’s database and changing it directly. — location: [1198](kindle://book?action=open&asin=B09B5L4NVT&location=1198) ^ref-48806

---
The differences between content coupling and common coupling are subtle. In both cases, two or more microservices are reading and writing to the same set of data. With common coupling, you understand that you are making use of a shared, external dependency. You know it’s not under your control. With content coupling, the lines of ownership become less clear, and it becomes more difficult for developers to change a system. — location: [1202](kindle://book?action=open&asin=B09B5L4NVT&location=1202) ^ref-5195

---
It’s certainly the case that the problems that occur with common coupling also apply with content coupling, but content coupling has some additional headaches that make it problematic enough that some people refer to it as pathological coupling. — location: [1227](kindle://book?action=open&asin=B09B5L4NVT&location=1227) ^ref-1140

---
Eric Evans’s Domain-Driven Design11 presented a series of important ideas that helped us better represent the problem domain in our programs. — location: [1244](kindle://book?action=open&asin=B09B5L4NVT&location=1244) ^ref-54581

---
Ubiquitous language Defining and adopting a common language to be used in code and in describing the domain, to aid communication. — location: [1247](kindle://book?action=open&asin=B09B5L4NVT&location=1247) ^ref-50899

---
Aggregate A collection of objects that are managed as a single entity, typically referring to real-world concepts. — location: [1248](kindle://book?action=open&asin=B09B5L4NVT&location=1248) ^ref-22107

---
Bounded context An explicit boundary within a business domain that provides functionality to the wider system but that also hides complexity. — location: [1249](kindle://book?action=open&asin=B09B5L4NVT&location=1249) ^ref-32966

---
The model that has always worked for me is to first consider an aggregate as a representation of a real domain concept—think of something like an Order, an Invoice, a Stock Item, and so on. — location: [1273](kindle://book?action=open&asin=B09B5L4NVT&location=1273) ^ref-30191

---
Aggregates typically have a life cycle around them, which opens them up to being implemented as a state machine. — location: [1274](kindle://book?action=open&asin=B09B5L4NVT&location=1274) ^ref-17174

---
We want to treat aggregates as self-contained units; we want to ensure that the code that handles the state transitions of an aggregate are grouped together, along with the state itself. — location: [1276](kindle://book?action=open&asin=B09B5L4NVT&location=1276) ^ref-39608

---
So one aggregate should be managed by one microservice, although a single microservice might own management of multiple aggregates. — location: [1278](kindle://book?action=open&asin=B09B5L4NVT&location=1278) ^ref-27920

---
In general, though, you should think of an aggregate as something that has state, identity, a life cycle that will be managed as part of the system. Aggregates typically refer to real-world concepts. — location: [1279](kindle://book?action=open&asin=B09B5L4NVT&location=1279) ^ref-58015

---
A single microservice will handle the life cycle and data storage of one or more different types of aggregates. — location: [1280](kindle://book?action=open&asin=B09B5L4NVT&location=1280) ^ref-18657

---
The key thing to understand here is that if an outside party requests a state transition in an aggregate, the aggregate can say no. You ideally want to implement your aggregates in such a way that illegal state transitions are impossible. — location: [1283](kindle://book?action=open&asin=B09B5L4NVT&location=1283) ^ref-32540

---
The benefits of this approach are twofold. The nature of the relationship is explicit, and in a REST system we could directly dereference this URI to look up the associated resource. — location: [1307](kindle://book?action=open&asin=B09B5L4NVT&location=1307) ^ref-17227

---
There are lots of ways to break a system into aggregates, with some choices being highly subjective. You may decide, for performance reasons or for ease of implementation, to reshape aggregates over time. I consider implementation concerns to be secondary, however; I begin by letting the mental model of the system users be my guiding light on initial design until other factors come into play. — location: [1314](kindle://book?action=open&asin=B09B5L4NVT&location=1314) ^ref-23258

---
Bounded Context A bounded context typically represents a larger organizational boundary. Within the scope of that boundary, explicit responsibilities need to be carried out. — location: [1318](kindle://book?action=open&asin=B09B5L4NVT&location=1318) ^ref-26522

---
Bounded contexts hide implementation detail. There are internal concerns—for example, the types of forklift trucks used are of little interest to anyone other than the folks in the warehouse. These internal concerns should be hidden from the outside world, which doesn’t need to know, nor should it care. — location: [1324](kindle://book?action=open&asin=B09B5L4NVT&location=1324) ^ref-18498

---
From an implementation point of view, bounded contexts contain one or more aggregates. Some aggregates may be exposed outside the bounded context; others may be hidden internally. — location: [1326](kindle://book?action=open&asin=B09B5L4NVT&location=1326) ^ref-49382

---
A shared model between the finance department and the warehouse — location: [1343](kindle://book?action=open&asin=B09B5L4NVT&location=1343) ^ref-12186

---
Mapping Aggregates and Bounded Contexts to Microservices Both the aggregate and the bounded context give us units of cohesion with well-defined interfaces with the wider system. — location: [1370](kindle://book?action=open&asin=B09B5L4NVT&location=1370) ^ref-18098

---
When starting out, as I’ve already mentioned, you want to reduce the number of services you work with. As a result, you should probably target services that encompass entire bounded contexts. — location: [1375](kindle://book?action=open&asin=B09B5L4NVT&location=1375) ^ref-10951

---
As you find your feet and decide to break these services into smaller services, you need to remember that aggregates themselves don’t want to be split apart—one microservice can manage one or more aggregates, but we don’t want one aggregate to be managed by more than one microservice. — location: [1376](kindle://book?action=open&asin=B09B5L4NVT&location=1376) ^ref-6895

---
The decision to decompose a service into smaller parts is arguably an implementation decision, so we might as well hide it if we can. In Figure 2-16 we see an example of this. We’ve split Warehouse down into Inventory and Shipping. As far as the outside world is concerned, there is still just the Warehouse microservice. Internally though, we’ve further decomposed things to allow Inventory to manage Stock Items and have Shipping manage Shipments. — location: [1385](kindle://book?action=open&asin=B09B5L4NVT&location=1385) ^ref-39906

---
It’s worth mentioning at this point that while the domain models defined through event storming can be used to implement event-driven systems—and indeed, the mapping is very straightforward—you can also use such a domain model to build a more request/response-oriented system. — location: [1409](kindle://book?action=open&asin=B09B5L4NVT&location=1409) ^ref-19099

---
The techies in the event storming session should be listening to what their nontechnical colleagues come up with here. A key part of this exercise is not to let any current implementation warp the perception of what the domain is (that comes later). At this stage you want to create a space in which you can get the concepts out of the heads of the key stakeholders and out in the open. — location: [1432](kindle://book?action=open&asin=B09B5L4NVT&location=1432) ^ref-4346

---
The noun here—“Order”—could well be a potential aggregate. And “Placed” describes something that can happen to an order, so this may well be part of the life cycle of the aggregate. Aggregates are represented by yellow sticky notes, and the commands and events associated with that aggregate are moved and clustered around the aggregate. This also helps you understand how aggregates are related to each other—events from one aggregate might trigger behavior in another. — location: [1436](kindle://book?action=open&asin=B09B5L4NVT&location=1436) ^ref-37381

---
Firstly, a big part of what makes DDD so powerful is that bounded contexts, which are so important to DDD, are explicitly about hiding information—presenting a clear boundary to the wider system while hiding internal complexity that is able to change without impacting other parts of the system. — location: [1448](kindle://book?action=open&asin=B09B5L4NVT&location=1448) ^ref-18820

---
This means that when we follow a DDD approach, whether we realize it or not, we are also adopting information hiding—and as we’ve seen, this is vital in helping to find stable microservice boundaries. — location: [1450](kindle://book?action=open&asin=B09B5L4NVT&location=1450) ^ref-27801

---
Secondly, the focus on defining a common, ubiquitous language helps greatly when it comes to defining microservice endpoints. — location: [1452](kindle://book?action=open&asin=B09B5L4NVT&location=1452) ^ref-11007

---
Fundamentally, DDD puts the business domain at the heart of the software we are building. The encouragement that it gives us to pull the language of the business into our code and service design helps improve domain expertise among the people who build the software. — location: [1458](kindle://book?action=open&asin=B09B5L4NVT&location=1458) ^ref-14987

---
This in turn helps build understanding and empathy for the users of our software and builds greater communication among technical delivery, product development, and the end users. — location: [1460](kindle://book?action=open&asin=B09B5L4NVT&location=1460) ^ref-41014

---
If you are interested in moving toward stream-aligned teams, DDD fits in neatly as a mechanism to help align the technical architecture with the wider organizational structure. — location: [1461](kindle://book?action=open&asin=B09B5L4NVT&location=1461) ^ref-36278

---
In fact, I often use multiple methods in conjunction with DDD to help identify how (and if) a system should be split. — location: [1470](kindle://book?action=open&asin=B09B5L4NVT&location=1470) ^ref-46405

---
It also avoids the fact that quite often changes in functionality require changes in “Systems of Record” (Mode 1) to allow for changes in “Systems of Innovation” (Mode 2). In my experience, organizations adopting bimodal IT do end up having two speeds—slow and slower. — location: [1494](kindle://book?action=open&asin=B09B5L4NVT&location=1494) ^ref-35146

---
Payment Card Industry (PCI) — location: [1507](kindle://book?action=open&asin=B09B5L4NVT&location=1507) ^ref-38161

---
Of course, we have to be aware of where this can drive us if adopted as a general means of decomposition. The classic three-tiered architecture that we discussed in the opening chapter, and that we show again in Figure 2-18, is an example of related technology being grouped together. As we’ve already explored, this is often a less than ideal architecture. Figure 2-18. A traditional three-tiered architecture is often driven by technological boundaries — location: [1531](kindle://book?action=open&asin=B09B5L4NVT&location=1531) ^ref-35031

---
It therefore follows that we must take into account the existing organizational structure when considering where and when to define boundaries, and in some situations we should perhaps even consider changing the organizational structure to support the architecture we want. — location: [1545](kindle://book?action=open&asin=B09B5L4NVT&location=1545) ^ref-58059

---
On the other hand, often organizational changes would just require that the owner of an existing microservice changes. — location: [1550](kindle://book?action=open&asin=B09B5L4NVT&location=1550) ^ref-20054

---
A better model would have been for the team in California to have one end-to-end vertical slice, consisting of the related parts of the frontend and data access functionality, with the team in Brazil taking another slice. — location: [1571](kindle://book?action=open&asin=B09B5L4NVT&location=1571) ^ref-47825

---
If you follow the guidelines of information hiding and appreciate the interplay of coupling and cohesion, then chances are you’ll avoid some of the worst pitfalls of whatever mechanism you pick. — location: [1586](kindle://book?action=open&asin=B09B5L4NVT&location=1586) ^ref-39681

---
The fact is, though, that there can often be reasons to mix models, even if “domain-oriented” is what you decide to pick as your main mechanism for defining microservice boundaries. — location: [1588](kindle://book?action=open&asin=B09B5L4NVT&location=1588) ^ref-41340

---
Organizational and domain-driven service boundaries are my own starting point. But that’s just my default approach. Typically, a number of the factors I’ve outlined here come into play, and which ones influence your own decisions will be based on the problems you are trying to solve. — location: [1596](kindle://book?action=open&asin=B09B5L4NVT&location=1596) ^ref-65436

---
If you want to go deeper, I can recommend Vaughn Vernon’s book Implementing Domain-Driven Design17 to help you understand the practicalities of this approach, while Vernon’s Domain-Driven Design Distilled18 is a great condensed overview if you’re looking for something more brief. — location: [1607](kindle://book?action=open&asin=B09B5L4NVT&location=1607) ^ref-16099

---
Fixating on microservices rather than on the end goal also means you will likely stop thinking of other ways in which you might bring about the change you are looking for. — location: [1665](kindle://book?action=open&asin=B09B5L4NVT&location=1665) ^ref-61261

---
Microservices aren’t easy. Try the simple stuff first. — location: [1669](kindle://book?action=open&asin=B09B5L4NVT&location=1669) ^ref-33297

---
Which microservice should you create first? Without an overarching understanding of what you are trying to achieve, you’re flying blind. — location: [1670](kindle://book?action=open&asin=B09B5L4NVT&location=1670) ^ref-36344

---
If you do a big-bang rewrite, the only thing you’re guaranteed of is a big bang. Martin Fowler — location: [1675](kindle://book?action=open&asin=B09B5L4NVT&location=1675) ^ref-13144

---
If you get to the point of deciding that breaking apart your existing monolithic system is the right thing to do, I strongly advise you to chip away at the monolith, extracting a bit at a time. An incremental approach will help you learn about microservices as you go and will also limit the impact of getting something wrong (and you will get things wrong!). — location: [1677](kindle://book?action=open&asin=B09B5L4NVT&location=1677) ^ref-36209

---
Break the big journey into lots of little steps. Each step can be carried out and learned from. If it turns out to be a retrograde step, it was only a small one. Either way, you learn from it, and the next step you take will be informed by those steps that came before. — location: [1682](kindle://book?action=open&asin=B09B5L4NVT&location=1682) ^ref-15969

---
Breaking things into smaller pieces also allows you to identify quick wins and learn from them. This can help make the next step easier and can help build momentum. — location: [1684](kindle://book?action=open&asin=B09B5L4NVT&location=1684) ^ref-49251

---
By splitting out microservices one at a time, you also get to unlock the value they bring incrementally, rather than having to wait for some big bang deployment. — location: [1685](kindle://book?action=open&asin=B09B5L4NVT&location=1685) ^ref-22399

---
All of this leads to what has become my stock advice for people looking at microservices: if you think microservices are a good idea, start somewhere small. Choose one or two areas of functionality, implement them as microservices, get them deployed into production, and then reflect on whether creating your new microservices helped you get closer to your end goal. — location: [1686](kindle://book?action=open&asin=B09B5L4NVT&location=1686) ^ref-5775

---
Warning You won’t appreciate the true horror, pain, and suffering that a microservice architecture can bring until you are running in production. — location: [1689](kindle://book?action=open&asin=B09B5L4NVT&location=1689) ^ref-36631

---
While I already made the case at the start of the book that some form of monolithic architecture can be a totally valid choice, it warrants repeating that a monolithic architecture isn’t inherently bad and therefore shouldn’t be viewed as the enemy. — location: [1692](kindle://book?action=open&asin=B09B5L4NVT&location=1692) ^ref-11799

---
It is common for the existing monolithic architecture to remain after a shift toward microservices, albeit often in a diminished capacity. — location: [1696](kindle://book?action=open&asin=B09B5L4NVT&location=1696) ^ref-57771

---
There is danger in creating microservices when you have an unclear understanding of the domain. — location: [1710](kindle://book?action=open&asin=B09B5L4NVT&location=1710) ^ref-60808

---
Prematurely decomposing a system into microservices can be costly, especially if you are new to the domain. In many ways, having an existing codebase you want to decompose into microservices is much easier than trying to go to microservices from the beginning for this very reason. — location: [1721](kindle://book?action=open&asin=B09B5L4NVT&location=1721) ^ref-6621

---
Fundamentally, the decision about which functionality to split into a microservice will end up being a balance between these two forces—how easy the extraction is versus the benefit of extracting the microservice in the first place. — location: [1737](kindle://book?action=open&asin=B09B5L4NVT&location=1737) ^ref-16025

---
It is important with a transition like this, especially one that could take months or years, to gain a sense of momentum early on. So you need some quick wins under your belt. — location: [1741](kindle://book?action=open&asin=B09B5L4NVT&location=1741) ^ref-32011

---
step. I will sound a note of caution here about ignoring the user interface part of the equation. I’ve seen far too many organizations look only at the benefits of decomposing the backend functionality, which often results in an overly siloed approach to any architectural restructuring. Sometimes the biggest benefits can come from decomposition of the UI, so ignore this at your peril. — location: [1753](kindle://book?action=open&asin=B09B5L4NVT&location=1753) ^ref-40582

---
Often decomposition of the UI tends to lag behind decomposition of the backend into microservices, since until the microservices are available, it’s difficult to see the possibilities for UI decomposition; just make sure it doesn’t lag too much. — location: [1756](kindle://book?action=open&asin=B09B5L4NVT&location=1756) ^ref-35226

---
In Figure 3-3, we have extracted the code associated with the wishlist functionality into a new microservice. The data for the wishlist remains in the monolithic database at this stage—we haven’t completed the decomposition until we’ve also moved out the data related to the new Wishlist microservice. Figure 3-3. Moving the wishlist code into a new microservice first, leaving the data in the monolithic database In my experience, this tends to be the most common first step. The main reason for this is that it tends to deliver more short-term benefit. — location: [1764](kindle://book?action=open&asin=B09B5L4NVT&location=1764) ^ref-43727

---
If we left the data in the monolithic database, we’re storing up lots of pain for the future, so that does need to be addressed too, but we have gained a lot from our new microservice. — location: [1770](kindle://book?action=open&asin=B09B5L4NVT&location=1770) ^ref-715

---
Extracting the application code tends to be easier than extracting things from the database. If we found that it was impossible to extract the application code cleanly, we could abort any further work, avoiding the need to detangle the database. — location: [1772](kindle://book?action=open&asin=B09B5L4NVT&location=1772) ^ref-16225

---
If, however, the application code is cleanly extracted but extracting the data proves to be impossible, we could be in trouble—thus it’s essential that even if you decide to extract the application code before the data, you need to have looked at the associated data storage and have some idea as to whether extraction is viable and how you will go about it. So do the legwork to sketch out how both application code and data will be extracted before you start. — location: [1773](kindle://book?action=open&asin=B09B5L4NVT&location=1773) ^ref-58054

---
The main benefit of this approach in the short term is in derisking the full extraction of the microservice. It forces you to deal up front with issues like loss of enforced data integrity in your database or lack of transactional operations across both sets of data. We’ll touch briefly on the implications of both issues later in this chapter. — location: [1783](kindle://book?action=open&asin=B09B5L4NVT&location=1783) ^ref-50757

---
Databases, especially relational databases, are good at joining data across different tables. Very good. So good, in fact, that we take this for granted. Often, though, when we split databases apart in the name of microservices, we end up having to move join operations from the data tier up into the microservices themselves. And try as we might, it’s unlikely to be as fast. — location: [1825](kindle://book?action=open&asin=B09B5L4NVT&location=1825) ^ref-50986

---
The join has gone from the data tier to the application code tier. Unfortunately, this operation isn’t going to be anywhere near as efficient as it would have been had the join remained in the database. — location: [1857](kindle://book?action=open&asin=B09B5L4NVT&location=1857) ^ref-61255

---
To an extent, you’ll simply need to get used to the fact that you can no longer rely on your database to enforce the integrity of inter-entity relationships. Obviously, for data that remains inside a single database, this isn’t an issue. — location: [1880](kindle://book?action=open&asin=B09B5L4NVT&location=1880) ^ref-51546

---
There are a number of work-arounds, although “coping patterns” would be a better term for ways we might deal with this problem. We could use a soft delete in the Album table so that we don’t actually remove a record but just mark it as deleted. — location: [1882](kindle://book?action=open&asin=B09B5L4NVT&location=1882) ^ref-44167

---
Another option could be to copy the name of the album into the Ledger table when a sale is made, but we would have to resolve how we wanted to handle synchronizing changes in the album name. — location: [1884](kindle://book?action=open&asin=B09B5L4NVT&location=1884) ^ref-28891

---
Once we start splitting data across multiple databases, though, we lose the safety of the ACID transactions we are used to. — location: [1889](kindle://book?action=open&asin=B09B5L4NVT&location=1889) ^ref-8268

---
distributed transactions are not only complex to implement, even when done well, but they also don’t actually give us the same guarantees that we came to expect with more narrowly scoped database transactions. — location: [1894](kindle://book?action=open&asin=B09B5L4NVT&location=1894) ^ref-51696

---
As with data integrity, we have to come to terms with the fact that by breaking apart our databases for what may be very good reasons, we will encounter a new set of problems. — location: [1898](kindle://book?action=open&asin=B09B5L4NVT&location=1898) ^ref-64141

---
With code, we have refactoring tooling built into our IDEs, and we have the added benefit that the systems we are changing are fundamentally stateless. With a database, the things we are changing have state, and we also lack good refactoring-type tooling. — location: [1902](kindle://book?action=open&asin=B09B5L4NVT&location=1902) ^ref-5154

---
However, as this is not a direct mapping, it creates the opportunity to come up with a schema design for the reporting database that is tailored exactly to the requirements of the consumers—this could involve using a radically different schema, or perhaps even a different type of database technology altogether. — location: [1924](kindle://book?action=open&asin=B09B5L4NVT&location=1924) ^ref-33994

---
The second key point is that the reporting database should be treated like any other microservice endpoint, and it is the job of the microservice maintainer to ensure that compatibility of this endpoint is maintained even if the microservice changes its internal implementation detail. The mapping from internal state to reporting database is the responsibility of the people who develop the microservice itself. — location: [1927](kindle://book?action=open&asin=B09B5L4NVT&location=1927) ^ref-9375

---
At one level, we can ignore this distinction. It’s easy, for example, to think of one object making a method call on another object and then just map this interaction to two microservices communicating via a network. Putting aside the fact that microservices aren’t just objects, this thinking can get us into a lot of trouble. — location: [1961](kindle://book?action=open&asin=B09B5L4NVT&location=1961) ^ref-44367

---
This can often lead you to want to rethink APIs. An API that makes sense in-process may not make sense in inter-process situations. I can make one thousand calls across an API boundary in-process without concern. Do I want to make one thousand network calls between two microservices? Perhaps not. — location: [1971](kindle://book?action=open&asin=B09B5L4NVT&location=1971) ^ref-62332

---
When making calls between microservices over a network, on the other hand, the data actually has to be serialized into some form that can be transmitted over a network. The data then needs to be sent and deserialized at the other end. We therefore may need to be more mindful about the size of payloads being sent between processes. — location: [1975](kindle://book?action=open&asin=B09B5L4NVT&location=1975) ^ref-24151

---
When was the last time you were aware of the size of a data structure that you were passing around inside a process? The reality is that you likely didn’t need to know; now you do. This might lead you to reduce the amount of data being sent or received (perhaps not a bad thing if we think about information hiding), pick more efficient serialization mechanisms, or even offload data to a filesystem and pass around a reference to that file location instead. — location: [1978](kindle://book?action=open&asin=B09B5L4NVT&location=1978) ^ref-48563

---
I’ve seen a lot of attempts to hide from the developer the fact that a network call is even taking place. Our desire to create abstractions to hide detail is a big part of what allows us to do more things more efficiently, but sometimes we create abstractions that hide too much. A developer needs to be aware if they are doing something that will result in a network call; otherwise, you should not be surprised if you end up with some nasty performance bottlenecks further down the line caused by odd inter-service interactions that weren’t visible to the developer writing the code. — location: [1982](kindle://book?action=open&asin=B09B5L4NVT&location=1982) ^ref-10118

---
In fact, if I change a method signature using an IDE with refactoring capability, often the IDE itself will automatically refactor calls to this changing method. — location: [1988](kindle://book?action=open&asin=B09B5L4NVT&location=1988) ^ref-584

---
When making a backward-incompatible change to a microservice interface, we either need to do a lockstep deployment with consumers, making sure they are updated to use the new interface, or else find some way to phase the rollout of the new microservice contract. — location: [1992](kindle://book?action=open&asin=B09B5L4NVT&location=1992) ^ref-33456

---
Arbitrary failure Otherwise known as Byzantine failure, this is when something has gone wrong, but participants are unable to agree if the failure has occurred (or why). As it sounds like, this is a bad time all around. — location: [2010](kindle://book?action=open&asin=B09B5L4NVT&location=2010) ^ref-39371

---
it can become important to have a richer set of semantics for returning errors in a way that can allow clients to take appropriate action. — location: [2016](kindle://book?action=open&asin=B09B5L4NVT&location=2016) ^ref-753

---
HTTP is an example of a protocol that understands the importance of this. Every HTTP response has a code, with the 400 and 500 series codes being reserved for errors. — location: [2017](kindle://book?action=open&asin=B09B5L4NVT&location=2017) ^ref-59787

---
400 series error codes are request errors—essentially, a downstream service is telling the client that there is something wrong with the original request. As such, it’s probably something you should give up on—is there any point retrying a 404 Not Found, for example? — location: [2018](kindle://book?action=open&asin=B09B5L4NVT&location=2018) ^ref-57161

---
The 500 series response codes relate to downstream issues, a subset of which indicate to the client that the issue might be temporary. A 503 Service Unavailable, for example, indicates that the downstream server is unable to handle the request, but it may be a temporary state, in which case an upstream client might decide to retry the request. On the other hand, if a client receives a 501 Not Implemented response, a retry is unlikely to help much. — location: [2020](kindle://book?action=open&asin=B09B5L4NVT&location=2020) ^ref-18667

---
Whether or not you pick an HTTP-based protocol for communication between microservices, if you have a rich set of semantics around the nature of the error, you’ll make it easier for clients to carry out compensating actions, which in turn should help you build more robust systems. — location: [2024](kindle://book?action=open&asin=B09B5L4NVT&location=2024) ^ref-64039

---
The range of technology available to us for inter-process communication is vast. As a result, we can often be overburdened with choice. — location: [2032](kindle://book?action=open&asin=B09B5L4NVT&location=2032) ^ref-25274

---
when you buy into a specific technology choice, you are often buying into a set of ideas and constraints that come along for the ride. These constraints might not be the right ones for you—and the mindset behind the technology may not actually line up with the problem you are trying to solve. — location: [2035](kindle://book?action=open&asin=B09B5L4NVT&location=2035) ^ref-36233

---
I see technology used in the wrong place time and time again. People pick the shiny new tech (like microservices!) without considering whether it actually fits their problem. — location: [2039](kindle://book?action=open&asin=B09B5L4NVT&location=2039) ^ref-57636

---
When using this model to help teams decide on the right approach, I spend a lot of time understanding the context in which they are operating. Their needs in terms of reliable communication, acceptable latency, and volume of communication are all going to play a part in making a technology choice. — location: [2061](kindle://book?action=open&asin=B09B5L4NVT&location=2061) ^ref-31522

---
But in general, I tend to start with deciding whether a request-response or an event-driven style of collaboration is more appropriate for the given situation. — location: [2063](kindle://book?action=open&asin=B09B5L4NVT&location=2063) ^ref-38743

---
A host of other considerations come into play when picking the right technology that go beyond the style of communication—for example, the need for lower-latency communication, security-related aspects, or the ability to scale. — location: [2066](kindle://book?action=open&asin=B09B5L4NVT&location=2066) ^ref-4491

---
It’s important to note that a microservice architecture as a whole may have a mix of styles of collaboration, and this is typically the norm. Some interactions just make sense as request-response, while others make sense as event-driven. — location: [2071](kindle://book?action=open&asin=B09B5L4NVT&location=2071) ^ref-26026

---
In fact, it’s common for a single microservice to implement more than one form of collaboration. — location: [2074](kindle://book?action=open&asin=B09B5L4NVT&location=2074) ^ref-38685

---
So if the Loyalty microservice wants to send a response back to Order Processor, but the upstream instance has subsequently died, the response will get lost. The temporal coupling here isn’t just between two microservices; it’s between two specific instances of these microservices. — location: [2105](kindle://book?action=open&asin=B09B5L4NVT&location=2105) ^ref-25943

---
Thus the use of synchronous calls can make a system vulnerable to cascading issues caused by downstream outages more readily than can the use of asynchronous calls. — location: [2112](kindle://book?action=open&asin=B09B5L4NVT&location=2112) ^ref-55154

---
To improve this situation, we could reexamine the interactions between the microservices in the first place. — location: [2132](kindle://book?action=open&asin=B09B5L4NVT&location=2132) ^ref-13778

---
Advantages With nonblocking asynchronous communication, the microservice making the initial call and the microservice (or microservices) receiving the call are decoupled temporarily. — location: [2157](kindle://book?action=open&asin=B09B5L4NVT&location=2157) ^ref-37958

---
The main downsides of nonblocking asynchronous communication, relative to blocking synchronous communication, are the level of complexity and the range of choice. — location: [2178](kindle://book?action=open&asin=B09B5L4NVT&location=2178) ^ref-20066

---
When we start digging into how these different styles of communication are implemented, there is a potentially bewildering list of technology we could look at. — location: [2180](kindle://book?action=open&asin=B09B5L4NVT&location=2180) ^ref-25245

---
If asynchronous communication doesn’t map to your mental models of computing, adopting an asynchronous style of communication will be challenging at first. And as we’ll explore further when we look in detail at the various styles of asynchronous communication, there are a lot of different, interesting ways in which you can get yourself into a lot of trouble. — location: [2181](kindle://book?action=open&asin=B09B5L4NVT&location=2181) ^ref-46541

---
So even if the underlying technology we are using to get the rate could be considered asynchronous in nature (for example, waiting for the rate), from the point of our code, this is inherently a synchronous, blocking interaction. — location: [2233](kindle://book?action=open&asin=B09B5L4NVT&location=2233) ^ref-21060

---
This pattern is in some ways the most common general inter-process communication pattern that you’ll see, and yet we sometimes fail to see it as a communication pattern at all—I think largely because the communication between processes is often so indirect as to be hard to spot. — location: [2256](kindle://book?action=open&asin=B09B5L4NVT&location=2256) ^ref-7142

---
It’s worth noting that any downstream microservice that is going to act on this data will need its own mechanism to identify that new data is available—polling is a frequent solution to this problem. — location: [2261](kindle://book?action=open&asin=B09B5L4NVT&location=2261) ^ref-48245

---
The use of prevalent and well-understood technology also enables interoperability between different types of systems, including older mainframe applications or customizable off-the-shelf (COTS) software products. Data volumes are also less of a concern here—if you’re sending lots of data in one big go, this pattern can work well. — location: [2280](kindle://book?action=open&asin=B09B5L4NVT&location=2280) ^ref-39631

---
If you are interested in sending larger volumes of data and having them processed more in “real time,” then using some sort of streaming technology like Kafka would be a better fit. — location: [2291](kindle://book?action=open&asin=B09B5L4NVT&location=2291) ^ref-19131

---
Another major sweet spot for this pattern is in sharing large volumes of data. If you need to send a multigigabyte file to a filesystem or load a few million rows into a database, then this pattern is the way to go. — location: [2304](kindle://book?action=open&asin=B09B5L4NVT&location=2304) ^ref-10532

---
When using a queue, we have the added benefit that multiple requests could be buffered up in the queue waiting to be handled. This can help in situations in which the requests can’t be handled quickly enough. — location: [2358](kindle://book?action=open&asin=B09B5L4NVT&location=2358) ^ref-13744

---
When a microservice receives a response in this way, it might need to relate the response to the original request. This can be challenging, as a lot of time may have passed, and depending on the nature of the protocol being used, the response may not come back to the same instance of the microservice that sent the request. In our example of reserving stock as part of placing an order, we’d need to know how to associate the “stock reserved” response with a given order so we can carry on processing that particular order. An easy way to handle this would be to store any state associated with the original request into a database, such that when the response comes in, the receiving instance can reload any associated state and act accordingly. — location: [2361](kindle://book?action=open&asin=B09B5L4NVT&location=2361) ^ref-27665

---
Eventually, we tracked down the problem. A bug had crept in whereby a certain type of pricing request would cause a worker to crash. We were using a transacted queue: as the worker died, its lock on the request timed out, and the pricing request was put back on the queue—only for another worker to pick it up and die. This was a classic example of what Martin Fowler calls a catastrophic failover. — location: [2561](kindle://book?action=open&asin=B09B5L4NVT&location=2561) ^ref-52124

---
The associated complexity with event-driven architectures and asynchronous programming in general leads me to believe that you should be cautious in how eagerly you start adopting these ideas. Ensure you have good monitoring in place, and strongly consider the use of correlation IDs, which allow you to trace requests across process boundaries, — location: [2568](kindle://book?action=open&asin=B09B5L4NVT&location=2568) ^ref-60381

---
We also have to be honest, though, about the integration styles that we might consider “simpler”—the problems associated with knowing whether things worked or not is not limited to asynchronous forms of integration. With a synchronous, blocking call, if you get a time-out, did this happen because the request got lost and the downstream party didn’t receive it? Or did the request get through, but the response got lost? What do you do in that situation? If you retry, but the original request did get through what then? (Well, this is where idempotency comes in, — location: [2574](kindle://book?action=open&asin=B09B5L4NVT&location=2574) ^ref-31086

---
My own biases toward asynchronous, event-driven collaboration are a function not just of my experiences but also of my aversion to coupling in general. But this style of communication comes with significant complexity that cannot be ignored, and every situation is unique. — location: [2585](kindle://book?action=open&asin=B09B5L4NVT&location=2585) ^ref-14380

---
Remote procedure call (RPC) refers to the technique of making a local call and having it execute on a remote service somewhere. There are a number of different RPC implementations in use. Most of the technology in this space requires an explicit schema, such as SOAP or gRPC. — location: [2658](kindle://book?action=open&asin=B09B5L4NVT&location=2658) ^ref-56929

---
In the context of RPC, the schema is often referred to as an interface definition language (IDL), with SOAP referring to its schema format as a web service definition language (WSDL). — location: [2662](kindle://book?action=open&asin=B09B5L4NVT&location=2662) ^ref-2850

---
All these technologies, however, have the same core characteristic: they make a remote call look like a local call. Typically, using an RPC technology means you are buying into a serialization protocol. The RPC framework defines how data is serialized and deserialized. — location: [2667](kindle://book?action=open&asin=B09B5L4NVT&location=2667) ^ref-16190

---
For instance, gRPC uses the protocol buffer serialization format for this purpose. Some implementations are tied to a specific networking protocol (like SOAP, which makes nominal use of HTTP), whereas others might allow you to use different types of networking protocols, which can provide additional features. For example, TCP offers guarantees about delivery, whereas UDP doesn’t but has a much lower overhead. This can allow you to use different networking technology for different use cases. — location: [2669](kindle://book?action=open&asin=B09B5L4NVT&location=2669) ^ref-2912

---
The ease of generation of client-side code is one of the main selling points of RPC. The fact that I can just make a normal method call and theoretically ignore the rest is a huge boon. — location: [2676](kindle://book?action=open&asin=B09B5L4NVT&location=2676) ^ref-36726

---
In a way, this technology coupling can be a form of exposing internal technical implementation details. For example, the use of RMI ties not only the client to the JVM but the server as well. To be fair, there are a number of RPC implementations that don’t have this restriction—gRPC, SOAP, and Thrift are all examples that allow for interoperability between different technology stacks. — location: [2686](kindle://book?action=open&asin=B09B5L4NVT&location=2686) ^ref-28403

---
The core idea of RPC is to hide the complexity of a remote call. However, this can lead to hiding too much. The drive in some forms of RPC to make remote method calls look like local method calls hides the fact that these two things are very different. — location: [2690](kindle://book?action=open&asin=B09B5L4NVT&location=2690) ^ref-37581

---
This means you need to think differently about API design for remote interfaces versus local interfaces. Just taking a local API and trying to make it a service boundary without any more thought is likely to get you in trouble. — location: [2694](kindle://book?action=open&asin=B09B5L4NVT&location=2694) ^ref-23081

---
In some of the worst examples, developers may be using remote calls without knowing it, if the abstraction is overly opaque. — location: [2696](kindle://book?action=open&asin=B09B5L4NVT&location=2696) ^ref-20763

---
You need to think about the network itself. Famously, the first of the fallacies of distributed computing is “The network is reliable”. Networks aren’t reliable. — location: [2697](kindle://book?action=open&asin=B09B5L4NVT&location=2697) ^ref-60624

---
The reality is that changes like this are fairly common. RPC endpoints often end up having a large number of methods for different ways of creating or interacting with objects. This is due in part to the fact that we are still thinking of these remote calls as local ones. — location: [2742](kindle://book?action=open&asin=B09B5L4NVT&location=2742) ^ref-61290

---
This is a key challenge with any RPC mechanism that promotes the use of binary stub generation: you don’t get to separate client and server deployments. If you use this technology, lockstep releases may be in your future. — location: [2763](kindle://book?action=open&asin=B09B5L4NVT&location=2763) ^ref-52103

---
In practice, objects used as part of binary serialization across the wire can be thought of as “expand-only” types. This brittleness results in the types being exposed over the wire and becoming a mass of fields, some of which are no longer used but can’t be safely removed. — location: [2770](kindle://book?action=open&asin=B09B5L4NVT&location=2770) ^ref-62791

---
Despite its shortcomings, I actually quite like RPC, and the more modern implementations, such as gRPC, are excellent, — location: [2773](kindle://book?action=open&asin=B09B5L4NVT&location=2773) ^ref-58771

---
Java RMI, for example, has a number of issues regarding brittleness and limited technology choices, and SOAP is pretty heavyweight from a developer perspective, especially when compared with more modern choices. — location: [2775](kindle://book?action=open&asin=B09B5L4NVT&location=2775) ^ref-33221

---
If I was looking at options in this space, gRPC would be at the top of my list. Built to take advantage of HTTP/2, it has some impressive performance characteristics and good general ease of use. — location: [2781](kindle://book?action=open&asin=B09B5L4NVT&location=2781) ^ref-25967

---
gRPC fits a synchronous request-response model well but can also work in conjunction with reactive extensions. It’s high on my list whenever I’m in situations where I have a good deal of control over both the client and server ends of the spectrum. — location: [2784](kindle://book?action=open&asin=B09B5L4NVT&location=2784) ^ref-19535

---
If you’re having to support a wide variety of other applications that might need to talk to your microservices, the need to compile client-side code against a server-side schema can be problematic. In that case, some form of REST over HTTP API would likely be a better fit. — location: [2785](kindle://book?action=open&asin=B09B5L4NVT&location=2785) ^ref-38498

---
Most important when thinking about REST is the concept of resources. You can think of a resource as a thing that the service itself knows about, like a Customer. — location: [2795](kindle://book?action=open&asin=B09B5L4NVT&location=2795) ^ref-28749

---
The server creates different representations of this Customer on request. How a resource is shown externally is completely decoupled from how it is stored internally. — location: [2796](kindle://book?action=open&asin=B09B5L4NVT&location=2796) ^ref-8995

---
There are many different styles of REST, and I touch only briefly on them here. I strongly recommend you take a look at the Richardson Maturity Model, where the different styles of REST are compared. — location: [2801](kindle://book?action=open&asin=B09B5L4NVT&location=2801) ^ref-17962

---
REST itself doesn’t really talk about underlying protocols, although it is most commonly used over HTTP. — location: [2803](kindle://book?action=open&asin=B09B5L4NVT&location=2803) ^ref-28697

---
Some of the features that HTTP gives us as part of the specification, such as verbs, make implementing REST over HTTP easier, whereas with other protocols you’ll have to handle these features yourself. — location: [2804](kindle://book?action=open&asin=B09B5L4NVT&location=2804) ^ref-53097

---
Conceptually, there is one endpoint in the form of a Customer resource in these cases, and the operations we can carry out on it are baked into the HTTP protocol. — location: [2814](kindle://book?action=open&asin=B09B5L4NVT&location=2814) ^ref-32827

---
Note that HTTP can be used to implement RPC too. SOAP, for example, gets routed over HTTP, but it unfortunately uses very little of the specification. Verbs are ignored, as are simple things like HTTP error codes. — location: [2822](kindle://book?action=open&asin=B09B5L4NVT&location=2822) ^ref-51483

---
On the other hand, gRPC has been designed to take advantage of the capabilities of HTTP/2, such as the ability to send multiple request-response streams over a single connection. — location: [2823](kindle://book?action=open&asin=B09B5L4NVT&location=2823) ^ref-36146

---
We have an understanding of what a shopping cart means, even if the exact form and underlying control used to represent it have changed. We know that if we want to view the cart, this is the control we want to interact with. This is how web pages can change incrementally over time. As long as these implicit contracts between the customer and the website are still met, changes don’t need to be breaking changes. — location: [2840](kindle://book?action=open&asin=B09B5L4NVT&location=2840) ^ref-43287

---
The theory is that, by using these controls to decouple the client and server, we gain significant benefits over time that hopefully offset the increase in the time it takes to get these protocols up and running. — location: [2883](kindle://book?action=open&asin=B09B5L4NVT&location=2883) ^ref-9567

---
Unfortunately, although these ideas all seem sensible in theory, I’ve found that this form of REST is rarely practiced, for reasons I’ve not entirely come to grips with. This makes HATEOAS in particular a much harder concept for me to promote for those already committed to the use of REST. — location: [2885](kindle://book?action=open&asin=B09B5L4NVT&location=2885) ^ref-54850

---
Fundamentally, many of the ideas in REST are predicated on creating distributed hypermedia systems, and this isn’t what most people end up building. — location: [2887](kindle://book?action=open&asin=B09B5L4NVT&location=2887) ^ref-41916

---
The OpenAPI specification that grew out of the Swagger project now provides you with the ability to define enough information on a REST endpoint to allow for the generation of client-side code in a variety of languages. — location: [2895](kindle://book?action=open&asin=B09B5L4NVT&location=2895) ^ref-64614

---
I do also have concerns about a specification that was previously used just for documentation now being used to define a more explicit contract. This can lead to a much more complex specification—comparing an OpenAPI schema with a protocol buffer schema, for example, is quite a stark contrast. Despite my reservations, though, it’s good that this option now exists. — location: [2898](kindle://book?action=open&asin=B09B5L4NVT&location=2898) ^ref-5636

---
It’s likely to be several years before HTTP/3 has a widespread impact on the public internet, but it seems reasonable to assume that organizations can benefit earlier than this within their own networks. — location: [2908](kindle://book?action=open&asin=B09B5L4NVT&location=2908) ^ref-762

---
With respect to HATEOAS specifically, you can encounter additional performance issues. As clients need to navigate multiple controls to find the right endpoints for a given operation, this can lead to very chatty protocols—multiple round trips may be required for each operation. — location: [2910](kindle://book?action=open&asin=B09B5L4NVT&location=2910) ^ref-46981

---
Ultimately, this is a trade-off. If you decide to adopt a HATEOAS-style of REST, I would suggest you start by having your clients navigate these controls first and then optimize later if necessary. — location: [2912](kindle://book?action=open&asin=B09B5L4NVT&location=2912) ^ref-42932

---
It would be a mistake to think of a REST API as just being a “good enough for most things” choice, but there is something to that. It’s a widely understood style of interface that most people are familiar with, and it guarantees interoperability from a huge variety of technologies. — location: [2923](kindle://book?action=open&asin=B09B5L4NVT&location=2923) ^ref-614

---
Due in large part to the capabilities of HTTP and the extent to which REST builds on these capabilities (rather than hiding them), REST-based APIs excel in situations in which you want large-scale and effective caching of requests. It’s for this reason that they are the obvious choice for exposing APIs to external parties or client interfaces. — location: [2925](kindle://book?action=open&asin=B09B5L4NVT&location=2925) ^ref-52648

---
They may well suffer, though, when compared to more efficient communication protocols, and although you can construct asynchronous interaction protocols over the top of REST-based APIs, that’s not really a great fit compared to the alternatives for general microservice-to-microservice communication. — location: [2927](kindle://book?action=open&asin=B09B5L4NVT&location=2927) ^ref-42794

---
My own experiences are obviously only one set of data points, and I don’t doubt that for some people HATEOAS may have worked well. But this concept does not seem to have caught on as much as I thought it would. — location: [2932](kindle://book?action=open&asin=B09B5L4NVT&location=2932) ^ref-9236

---
It’s also possible, of course, that the concepts behind HATEOAS don’t really mix well with how we build microservices. — location: [2935](kindle://book?action=open&asin=B09B5L4NVT&location=2935) ^ref-53253

---
So for use at the perimeter, it works fantastically well, and for synchronous request-response-based communication between microservices, it’s great. — location: [2936](kindle://book?action=open&asin=B09B5L4NVT&location=2936) ^ref-9229

---
In recent years, GraphQL has gained more popularity, due in large part to the fact that it excels in one specific area. Namely, it makes it possible for a client-side device to define queries that can avoid the need to make multiple requests to retrieve the same information. This can offer significant improvements in terms of the performance of constrained client-side devices and can also avoid the need to implement bespoke server-side aggregation. — location: [2939](kindle://book?action=open&asin=B09B5L4NVT&location=2939) ^ref-30072

---
Especially with mobile devices, this can be wasteful—it uses up more of a mobile device’s data plan than is needed, and it can take longer. GraphQL allows the mobile device to issue a single query that can pull back all the required information. — location: [2948](kindle://book?action=open&asin=B09B5L4NVT&location=2948) ^ref-19589

---
This GraphQL endpoint is the entry for all client queries and exposes a schema for the client devices to use. — location: [2951](kindle://book?action=open&asin=B09B5L4NVT&location=2951) ^ref-51504

---
The difference is that with SQL we at least have tools like query planners for our databases, which can help us diagnose problematic queries, whereas a similar problem with GraphQL can be harder to track down. — location: [2962](kindle://book?action=open&asin=B09B5L4NVT&location=2962) ^ref-2533

---
The advice I’ve seen on this issue seems to revolve around just associating an ID with every returned resource (and remember, a GraphQL query could contain multiple resources) and then having the client device cache the request against that ID. — location: [2967](kindle://book?action=open&asin=B09B5L4NVT&location=2967) ^ref-21242

---
If the queries you are issuing are highly specific in nature to a particular user, then this lack of request-level caching may not be a deal breaker, of course, as your cache-hit ratio is likely to be low. I do wonder, though, if this limitation means that you’ll still end up with a hybrid solution for client devices, with some (more generic) requests going over normal REST-based HTTP APIs and other requests going over GraphQL. — location: [2971](kindle://book?action=open&asin=B09B5L4NVT&location=2971) ^ref-26820

---
Another issue is that while GraphQL theoretically can handle writes, it doesn’t seem to fit as well as for reads. This leads to situations in which teams are using GraphQL for read but REST for writes. — location: [2974](kindle://book?action=open&asin=B09B5L4NVT&location=2974) ^ref-47511

---
Fundamentally, GraphQL is a call aggregation and filtering mechanism, so in the context of a microservice architecture it would be used to aggregate calls over multiple downstream microservices. — location: [2988](kindle://book?action=open&asin=B09B5L4NVT&location=2988) ^ref-26596

---
An alternative to the use of GraphQL would be to consider an alternative pattern like the backend for frontend (BFF) pattern—we’ll — location: [2990](kindle://book?action=open&asin=B09B5L4NVT&location=2990) ^ref-6757

---
Rather than one microservice directly communicating with another microservice, the microservice instead gives a message to a message broker, with information about how the message should be sent. — location: [3000](kindle://book?action=open&asin=B09B5L4NVT&location=3000) ^ref-15482

---
Brokers tend to provide either queues or topics, or both. — location: [3002](kindle://book?action=open&asin=B09B5L4NVT&location=3002) ^ref-39208

---
Queues are typically point to point. A sender puts a message on a queue, and a consumer reads from that queue. — location: [3003](kindle://book?action=open&asin=B09B5L4NVT&location=3003) ^ref-34050

---
With a topic-based system, multiple consumers are able to subscribe to a topic, and each subscribed consumer will receive a copy of that message. — location: [3004](kindle://book?action=open&asin=B09B5L4NVT&location=3004) ^ref-36671

---
Only one instance of each consumer group will see that event. — location: [3016](kindle://book?action=open&asin=B09B5L4NVT&location=3016) ^ref-2468

---
At first glance, a queue just looks like a topic with a single consumer group. A large part of the distinction between the two is that when a message is sent over a queue, there is knowledge of what the message is being sent to. With a topic, this information is hidden from the sender of the message—the sender is unaware of who (if anyone) will end up receiving the message. — location: [3017](kindle://book?action=open&asin=B09B5L4NVT&location=3017) ^ref-8592

---
Topics are a good fit for event-based collaboration, whereas queues would be more appropriate for request/response communication. This should be considered as general guidance rather than a strict rule, however. — location: [3020](kindle://book?action=open&asin=B09B5L4NVT&location=3020) ^ref-55537

---
From the point of view of the microservice sending the message, this can be very useful. It’s not a problem if the downstream destination is unavailable—the broker will hold on to the message until it can be delivered. This can reduce the number of things an upstream microservice needs to worry about. — location: [3029](kindle://book?action=open&asin=B09B5L4NVT&location=3029) ^ref-29333

---
There is typically a lot involved in running a broker correctly, partly due to the challenges in managing cluster-based software. — location: [3035](kindle://book?action=open&asin=B09B5L4NVT&location=3035) ^ref-53291

---
Often, the promise of guaranteed delivery can be undermined if the broker isn’t set up correctly. — location: [3036](kindle://book?action=open&asin=B09B5L4NVT&location=3036) ^ref-62350

---
all brokers have restrictions as to how they need to be run to deliver the promise of guaranteed delivery. — location: [3039](kindle://book?action=open&asin=B09B5L4NVT&location=3039) ^ref-57684

---
It’s also worth noting that what any given broker means by guaranteed delivery can vary. — location: [3040](kindle://book?action=open&asin=B09B5L4NVT&location=3040) ^ref-1151

---
If you’ve built a system that is based on the assumption that delivery is guaranteed, and that turns out not to be the case due to an issue with the underlying broker, it can cause significant issues. The hope, of course, is that you are offloading that work to software created by people who can do that job better than you can. — location: [3044](kindle://book?action=open&asin=B09B5L4NVT&location=3044) ^ref-9561

---
Some brokers can also provide read transactionality, something I’ve taken advantage of when using a number of brokers via the Java Message Service (JMS) APIs. This can be useful if you want to ensure the message can be processed by the consumer before removing it from the broker. — location: [3054](kindle://book?action=open&asin=B09B5L4NVT&location=3054) ^ref-14443

---
This is a complex topic, as I’ve spoken to some experts who state that guaranteeing exactly once delivery in all cases is impossible, while other experts say you basically can do so with a few simple workarounds. — location: [3059](kindle://book?action=open&asin=B09B5L4NVT&location=3059) ^ref-49961

---
build your consumers in such a way that they are prepared for the fact that they might receive a message more than once and can handle this situation. A very simple example would be for each message to have an ID, which a consumer can check each time a message is received. — location: [3061](kindle://book?action=open&asin=B09B5L4NVT&location=3061) ^ref-51617

---
SQS was in fact the second-ever product released by AWS, having been launched back in 2006. — location: [3072](kindle://book?action=open&asin=B09B5L4NVT&location=3072) ^ref-30468

---
Part of that popularity is due to Kafka’s use in helping move large volumes of data around as part of implementing stream processing pipelines. — location: [3075](kindle://book?action=open&asin=B09B5L4NVT&location=3075) ^ref-4367

---
With Kafka, messages can be stored for a configurable period. This means that messages can be stored forever. This can allow consumers to reingest messages that they had already processed, or allow newly deployed consumers to process messages that were sent previously. — location: [3082](kindle://book?action=open&asin=B09B5L4NVT&location=3082) ^ref-42074

---
some tasks can instead be done inside Kafka itself. Using KSQL, you can define SQL-like statements that can process one or more topics on the fly. This can give you something akin to a dynamically updating materialized database view, with the source of data being Kafka topics rather than a database. — location: [3086](kindle://book?action=open&asin=B09B5L4NVT&location=3086) ^ref-50375

---
It’s also worth pointing out that some of the simplicity of JSON comes at a cost—in our rush to adopt simpler protocols, schemas went out of the window (more on that later). — location: [3109](kindle://book?action=open&asin=B09B5L4NVT&location=3109) ^ref-56788

---
Avro is an interesting serialization format. It takes JSON as an underlying structure and uses it to define a schema-based format. Avro has found a lot of popularity as a format for message payloads, partly due to its ability to send the schema as part of the payload, which can make supporting multiple different messaging formats much easier. — location: [3110](kindle://book?action=open&asin=B09B5L4NVT&location=3110) ^ref-29434

---
In my experience, the vast majority of systems rarely have to worry about such optimizations, as they can often achieve the improvements they are looking for by sending less data or by not making the call at all. — location: [3130](kindle://book?action=open&asin=B09B5L4NVT&location=3130) ^ref-13375

---
As I’ve already discussed, I am in favor of having explicit schemas for microservice endpoints, for two key reasons. Firstly, they go a long way toward being an explicit representation of what a microservice endpoint exposes and what it can accept. This makes life easier both for developers working on the microservice and for their consumers. — location: [3141](kindle://book?action=open&asin=B09B5L4NVT&location=3141) ^ref-5156

---
Schemas may not replace the need for good documentation, but they certainly can help reduce the amount of documentation required. — location: [3144](kindle://book?action=open&asin=B09B5L4NVT&location=3144) ^ref-24881

---
The other reason I like explicit schemas, though, is how they help in terms of catching accidental breakages of microservice endpoints. — location: [3145](kindle://book?action=open&asin=B09B5L4NVT&location=3145) ^ref-60428

---
Broadly speaking, we can break contract breakages down into two categories—structural breakages and semantic breakages. — location: [3148](kindle://book?action=open&asin=B09B5L4NVT&location=3148) ^ref-23727

---
I’ve found myself to be very productive (relatively speaking) in both. Certainly, dynamically typed languages give you some significant benefits that for many people justify giving up on compile-time safety. — location: [3174](kindle://book?action=open&asin=B09B5L4NVT&location=3174) ^ref-39728

---
A lot of my desire for an explicit schema is driven by the fact that I think it’s important to be as explicit as possible about what a microservice does (or doesn’t) expose. — location: [3184](kindle://book?action=open&asin=B09B5L4NVT&location=3184) ^ref-22792

---
Ultimately, a lot of what schemas provide is an explicit representation of part of the structure contract between a client and a server. They help make things explicit and can greatly aid communication between teams as well as work as a safety net. — location: [3188](kindle://book?action=open&asin=B09B5L4NVT&location=3188) ^ref-37509

---
In situations in which the cost of change is reduced—for example, when both client and server are owned by the same team—I am more relaxed about not having schemas. — location: [3189](kindle://book?action=open&asin=B09B5L4NVT&location=3189) ^ref-33851

---
Postel’s law (otherwise known as the robustness principle), which states: “Be conservative in what you do, be liberal in what you accept from others.” — location: [3258](kindle://book?action=open&asin=B09B5L4NVT&location=3258) ^ref-7730

---
The original context for this piece of wisdom was the interaction of devices over networks, where you should expect all sorts of odd things to happen. In the context of microservice-based interactions, it leads us to try and structure our client code to be tolerant of changes to payloads. — location: [3259](kindle://book?action=open&asin=B09B5L4NVT&location=3259) ^ref-22817

---
an explicit schema goes a long way toward making the boundaries of information hiding more explicit—what’s exposed in the schema is by definition not hidden. — location: [3275](kindle://book?action=open&asin=B09B5L4NVT&location=3275) ^ref-49355

---
With semantic versioning, each version number is in the form MAJOR.MINOR.PATCH. When the MAJOR number increments, it means that backward-incompatible changes have been made. When MINOR increments, new functionality has been added that should be backward compatible. Finally, a change to PATCH states that bug fixes have been made to existing functionality. — location: [3294](kindle://book?action=open&asin=B09B5L4NVT&location=3294) ^ref-31640

---
This versioning scheme allows us to pack a lot of information and expectations into just three fields. The full specification outlines in very simple terms the expectations clients can have of changes to these numbers, and it can simplify the process of communicating about whether changes should impact consumers. Unfortunately, I haven’t seen this approach used enough in distributed systems to understand its effectiveness in that context—something that hasn’t really changed since the first edition of this book. — location: [3305](kindle://book?action=open&asin=B09B5L4NVT&location=3305) ^ref-8713

---
What you’re looking for, though, is something that won’t just report on the differences between two schemas but will pass or fail based on compatibility; this would allow you to fail a CI build if incompatible schemas are found, ensuring that your microservice won’t get deployed. — location: [3319](kindle://book?action=open&asin=B09B5L4NVT&location=3319) ^ref-31710

---
The open source Confluent Schema Registry supports JSON Schema, Avro, and protocol buffers and is capable of comparing newly uploaded versions for backward compatibility. Although it was built to help as part of an ecosystem in which Kafka is being used, and needs Kafka to run, there is nothing to stop you from using it to store and validate schemas being used for non-Kafka-based communication. — location: [3321](kindle://book?action=open&asin=B09B5L4NVT&location=3321) ^ref-63132

---
Just remember, if you don’t have schemas, expect your testing to have to do more work to catch breaking changes. — location: [3331](kindle://book?action=open&asin=B09B5L4NVT&location=3331) ^ref-40596

---
Another versioning solution often cited is to have different versions of the service live at once and for older consumers to route their traffic to the older version, with newer consumers seeing the new version, — location: [3352](kindle://book?action=open&asin=B09B5L4NVT&location=3352) ^ref-43014

---
First, if I need to fix an internal bug in my service, I now have to fix and deploy two different sets of services. This would probably mean I have to branch the codebase for my service, and that is always problematic. Second, it means I need smarts to handle directing consumers to the right microservice. — location: [3357](kindle://book?action=open&asin=B09B5L4NVT&location=3357) ^ref-28432

---
Finally, consider any persistent state our service might manage. Customers created by either version of the service need to be stored and made visible to all services, no matter which version was used to create the data in the first place. This can be an additional source of complexity. — location: [3361](kindle://book?action=open&asin=B09B5L4NVT&location=3361) ^ref-46988

---
Coexisting concurrent service versions for a short period of time can make perfect sense, especially when you’re doing something like a canary release (we’ll be discussing this pattern more in “On to Progressive Delivery”). In these situations, we may be coexisting versions for only a few minutes or perhaps hours, and we normally will have only two different versions of the service present at the same time. The longer it takes for you to get consumers upgraded to the newer version and released, the more you should look to coexist different endpoints in the same microservice rather than coexist entirely different versions. I remain unconvinced that this work is worthwhile for the average project. — location: [3365](kindle://book?action=open&asin=B09B5L4NVT&location=3365) ^ref-38668

---
This is in effect an example of the expand and contract pattern, which allows us to phase in breaking changes. We expand the capabilities we offer, supporting both old and new ways of doing something. Once the old consumers do things in the new way, we contract our API, removing the old functionality. — location: [3386](kindle://book?action=open&asin=B09B5L4NVT&location=3386) ^ref-56406

---
On the one hand, I like URIs being opaque to discourage clients from hardcoding URI templates, but on the other hand, this approach does make things very obvious and can simplify request routing. — location: [3391](kindle://book?action=open&asin=B09B5L4NVT&location=3391) ^ref-45288

---
Which Approach Do I Prefer? For situations in which the same team manages both the microservice and all consumers, I am somewhat relaxed about a lockstep release in limited situations. Assuming it really is a one-off situation, then doing this when the impact is limited to a single team can be justifiable. I am very cautious about this, though, as there is the danger that a one-off activity becomes business as usual, and there goes independent deployability. Use lockstep deployments too often, and you’ll end up with a distributed monolith before long. — location: [3396](kindle://book?action=open&asin=B09B5L4NVT&location=3396) ^ref-16746

---
Coexisting different versions of the same microservice can be problematic, as we discussed. I’d consider doing this only in situations in which we planned to run the microservice versions side by side for only a short period of time. — location: [3401](kindle://book?action=open&asin=B09B5L4NVT&location=3401) ^ref-30741

---
My general preference is to use emulation of old endpoints wherever possible. — location: [3405](kindle://book?action=open&asin=B09B5L4NVT&location=3405) ^ref-59929

---
I’ve found that in many situations, how these changes will be handled has never been discussed, leading to all sorts of challenges. As with schemas, having some degree of explicitness in how backward-incompatible changes will be made can greatly simplify things. — location: [3413](kindle://book?action=open&asin=B09B5L4NVT&location=3413) ^ref-59691

---
But assuming you aren’t going down the route of lockstep releases, I’d suggest that both the owner and the consumer of a microservice need to be clear on a few things: How will you raise the issue that the interface needs to change? How will the consumers and microservice teams collaborate to agree on what the change will look like? Who is expected to do the work to update the consumers? When the change is agreed on, how long will consumers have to shift over to the new interface before it is removed? — location: [3416](kindle://book?action=open&asin=B09B5L4NVT&location=3416) ^ref-60483

---
Remember, one of the secrets to an effective microservice architecture is to embrace a consumer-first approach. Your microservices exist to be called by other consumers. The consumers’ needs are paramount, and if you are making changes to a microservice that are going to cause upstream consumers problems, this needs to be taken into account. — location: [3421](kindle://book?action=open&asin=B09B5L4NVT&location=3421) ^ref-12257

---
I’ve heard from Netflix that they had issues (at least historically) with old set-top boxes using older versions of the Netflix APIs. These set-top boxes cannot be upgraded easily, so the old endpoints have to remain available unless and until the number of older set-top boxes drops to a level at which they can have their support disabled. — location: [3425](kindle://book?action=open&asin=B09B5L4NVT&location=3425) ^ref-28929

---
Decisions to stop old consumers from being able to access your endpoints can sometimes end up being financial ones—how much money does it cost you to support the old interface, balanced against how much money you make from those consumers. — location: [3427](kindle://book?action=open&asin=B09B5L4NVT&location=3427) ^ref-44209

---
Tracking Usage Even if you do agree on a time by which consumers should stop using the old interface, would you know if they had actually stopped using it? — location: [3430](kindle://book?action=open&asin=B09B5L4NVT&location=3430) ^ref-53761

---
This could be something as simple as asking consumers to put their identifer in the user-agent header when making HTTP requests, or you could require that all calls go via some sort of API gateway where clients need keys to identify themselves. — location: [3433](kindle://book?action=open&asin=B09B5L4NVT&location=3433) ^ref-4219

---
Personally, even if I was to suggest just turning the endpoint off after a certain period of time, I’d still definitely want tracking of who was going to be impacted. — location: [3445](kindle://book?action=open&asin=B09B5L4NVT&location=3445) ^ref-19562

---
The solution was to insert a sleep in the old library so that it responded more slowly to calls (with logging to show what was happening). Over time, the team driving the deprecation just kept increasing the duration of the sleep, until eventually the other teams got the message. You obviously have to be extremely sure that you’ve exhausted other reasonable efforts to get consumers to upgrade before considering something like — location: [3449](kindle://book?action=open&asin=B09B5L4NVT&location=3449) ^ref-11389

---
One of the acronyms we developers hear a lot is DRY: don’t repeat yourself. Though its definition is sometimes simplified as trying to avoid duplicating code, DRY more accurately means that we want to avoid duplicating our system behavior and knowledge. — location: [3456](kindle://book?action=open&asin=B09B5L4NVT&location=3456) ^ref-39399

---
When you want to change behavior, and that behavior is duplicated in many parts of your system, it is easy to forget everywhere you need to make a change, which can lead to bugs. So using DRY as a mantra in general makes sense. — location: [3461](kindle://book?action=open&asin=B09B5L4NVT&location=3461) ^ref-12255

---
Perhaps we go as far as making a shared library that we can use everywhere! It turns out, though, that sharing code in a microservice environment is a bit more involved than that. As always, we have more than one option to consider. — location: [3464](kindle://book?action=open&asin=B09B5L4NVT&location=3464) ^ref-13611

---
This library was used by all the services we had. But when a change was made to one of them, all services had to be updated. Our system communicated via message queues, which also had to be drained of their now invalid contents, and woe betide you if you forgot. — location: [3470](kindle://book?action=open&asin=B09B5L4NVT&location=3470) ^ref-37472

---
The really important point about sharing code via libraries is that you cannot update all uses of the library at once. Although multiple microservices might all use the same library, they do so typically by packaging that library into the microservice deployment. To upgrade the version of the library being used, you’d therefore need to redeploy the microservice. — location: [3475](kindle://book?action=open&asin=B09B5L4NVT&location=3475) ^ref-59748

---
If you want to update the same library everywhere at exactly the same time, it could lead to a widespread deployment of multiple different microservices all at the same time, with all the associated headaches. — location: [3478](kindle://book?action=open&asin=B09B5L4NVT&location=3478) ^ref-34595

---
These SDKs, though, are written by the wider community, or else by people inside AWS other than those who work on the API itself. This degree of separation seems to work and avoids some of the pitfalls of client libraries. Part of the reason this works so well is that the client is in charge of when the upgrade happens. If you go down the path of client libraries yourself, make sure this is the case. — location: [3495](kindle://book?action=open&asin=B09B5L4NVT&location=3495) ^ref-51056

---
In fact, the client libraries used by Netflix are as much if not more about ensuring reliability and scalability of their systems. The Netflix client libraries handle service discovery, failure modes, logging, and other aspects that aren’t actually about the nature of the service itself. Without these shared clients, it would be hard to ensure that each piece of client/server communications behaved well at the massive scale at which Netflix operates. — location: [3499](kindle://book?action=open&asin=B09B5L4NVT&location=3499) ^ref-10715

---
Their use at Netflix has certainly made it easy to get up and running and increase productivity while also ensuring the system behaves well. However, according to at least one person at Netflix, over time this has led to a degree of coupling between client and server that has been problematic. — location: [3502](kindle://book?action=open&asin=B09B5L4NVT&location=3502) ^ref-40776

---
And finally, make sure that the clients are in charge of when to upgrade their client libraries: we need to ensure we maintain the ability to release our services independently of each other! — location: [3507](kindle://book?action=open&asin=B09B5L4NVT&location=3507) ^ref-60693

---
Or perhaps you just want to make it easy for developers in your organization to know what APIs are available so they don’t reinvent the wheel. Broadly speaking, all of these use cases fall under the banner of service discovery. And as always with microservices, we have quite a few different options at our disposal for dealing with it. — location: [3516](kindle://book?action=open&asin=B09B5L4NVT&location=3516) ^ref-26486

---
All of the solutions we’ll look at handle things in two parts. First, they provide some mechanism for an instance to register itself and say, “I’m here!” Second, they provide a way to find the service once it’s registered. — location: [3519](kindle://book?action=open&asin=B09B5L4NVT&location=3519) ^ref-9739

---
Service discovery gets more complicated, though, when we are considering an environment in which we are constantly destroying and deploying new instances of services. Ideally, we’d want whatever solution we pick to cope with this. — location: [3520](kindle://book?action=open&asin=B09B5L4NVT&location=3520) ^ref-61108

---
DNS has a host of advantages, the main one being it is such a well-understood and well-used standard that almost any technology stack will support it. Unfortunately, while a number of services exist for managing DNS inside an organization, few of them seem designed for an environment in which we are dealing with highly disposable hosts, making updating DNS entries somewhat painful. — location: [3537](kindle://book?action=open&asin=B09B5L4NVT&location=3537) ^ref-19993

---
When we want to change the host to which the domain name refers, we update that entry, but we have to assume that clients will be holding on to the old IP for at least as long as the TTL states. DNS entries can get cached in multiple places (even the JVM will cache DNS entries unless you tell it not to), and the more places they are cached in, the more stale the entry can be. — location: [3543](kindle://book?action=open&asin=B09B5L4NVT&location=3543) ^ref-20731

---
One way to work around this problem is to have the domain name entry for your service point to a load balancer, which in turn points to the instances of your service, as shown in Figure 5-5. When you deploy a new instance, you can take the old one out of the load-balancer entry and add the new one. — location: [3546](kindle://book?action=open&asin=B09B5L4NVT&location=3546) ^ref-16025

---
Some people use DNS round-robining, where the DNS entries themselves refer to a group of machines. This technique is extremely problematic, as the client is hidden from the underlying host and therefore cannot easily stop routing traffic to one of the hosts should it become sick. — location: [3549](kindle://book?action=open&asin=B09B5L4NVT&location=3549) ^ref-64742

---
For a situation in which you have only single nodes, having DNS refer directly to hosts is probably fine. But for those situations in which you need more than one instance of a host, have DNS entries resolve to load balancers that can handle putting individual hosts into and out of service as appropriate. — location: [3554](kindle://book?action=open&asin=B09B5L4NVT&location=3554) ^ref-57046

---
If you’re running on a platform that manages container workloads for you, chances are you already have a service discovery mechanism provided for you. Kubernetes is no different, and it comes partly from etcd, a configuration management store bundled with Kubernetes. — location: [3594](kindle://book?action=open&asin=B09B5L4NVT&location=3594) ^ref-27701

---
in a nutshell, the way service discovery works on Kubernetes is that you deploy a container in a pod, and then a service dynamically identifies which pods should be part of a service by pattern matching on metadata associated with the pod. It’s a pretty elegant mechanism and can be very powerful. Requests to a service will then get routed to one of the pods that make up that service. — location: [3600](kindle://book?action=open&asin=B09B5L4NVT&location=3600) ^ref-41475

---
Nowadays, this is not the route I would go. The crop of tooling in this space is mature enough that this would be a case of not just reinventing the wheel but recreating a much worse wheel. — location: [3619](kindle://book?action=open&asin=B09B5L4NVT&location=3619) ^ref-59335

---
for our purposes we’ll talk more broadly about a networked perimeter. This could relate to an entire data center, a Kubernetes cluster, or perhaps just a virtual networking concept like a group of machines running on the same virtual LAN. — location: [3638](kindle://book?action=open&asin=B09B5L4NVT&location=3638) ^ref-12522

---
Speaking generally, an API gateway sits on the perimeter of your system and deals with north-south traffic. Its primary concerns are managing access from the outside world to your internal microservices. — location: [3640](kindle://book?action=open&asin=B09B5L4NVT&location=3640) ^ref-11583

---
Being focused more on north-south traffic, the API gateway’s main concern in a microservices environment is mapping requests from external parties to internal microservices. This responsibility is akin to what you could achieve with a simple HTTP proxy, and in fact API gateways typically build more features on top of existing HTTP proxy products, and they largely function as reverse proxies. — location: [3655](kindle://book?action=open&asin=B09B5L4NVT&location=3655) ^ref-18120

---
Part of the confusion around the API gateway has to do with history. A while back, there was a huge amount of interest in what was called “the API economy.” — location: [3659](kindle://book?action=open&asin=B09B5L4NVT&location=3659) ^ref-24502

---
This caused a number of people to start looking at the software they already had and consider the benefits of exposing that functionality to their customers not just via a GUI but also via an API. The hope was that this would open… — location: [3662](kindle://book?action=open&asin=B09B5L4NVT&location=3662) ^ref-26564

---
Amid this interest, a crop of API gateway products emerged to help make achieving those goals possible. Their featureset leaned heavily on managing API keys for third parties, enforcing rate… — location: [3664](kindle://book?action=open&asin=B09B5L4NVT&location=3664) ^ref-60817

---
The reality is that while APIs have absolutely been shown to be an excellent way to deliver services to some customers, the size of the API economy wasn’t quite as big as some had hoped, and a lot of companies found that they had purchased API… — location: [3666](kindle://book?action=open&asin=B09B5L4NVT&location=3666) ^ref-55644

---
The need for some form of an API gateway for Kubernetes is essential, as Kubernetes natively handles networking only within the cluster and does nothing about handling communication to and from the cluster itself. But in such a use case, an API… — location: [3670](kindle://book?action=open&asin=B09B5L4NVT&location=3670) ^ref-54311

---
So if you want an API gateway, be really clear in what you expect from it. In fact, I’d go a bit further and say that you should probably avoid having an API gateway… — location: [3672](kindle://book?action=open&asin=B09B5L4NVT&location=3672) ^ref-42174

---
If it’s just a case of exposing microservices running in Kubernetes, you could run your own reverse proxies—or better yet, you could look at a focused product like Ambassador, which was… — location: [3676](kindle://book?action=open&asin=B09B5L4NVT&location=3676) ^ref-33101

---
It’s possible, in fact, that you may end up with more than one gateway in the mix to better handle separation of concerns, and I can see that being sensible in many situations, although the usual caveats around increasing the overall… — location: [3678](kindle://book?action=open&asin=B09B5L4NVT&location=3678) ^ref-24599

---
I’ve put a lot of that down to VC-backed companies that had built a product for the boom times of the API economy, only to find that market doesn’t exist, and so they are fighting on two fronts: they are fighting over the small number of users that actually need what the more complex gateways are offering, while also losing business to… — location: [3683](kindle://book?action=open&asin=B09B5L4NVT&location=3683) ^ref-42893

---
Two key examples I’ve seen of misuse of API gateways is for call aggregation and protocol rewriting, but I’ve also seen a wider push to use API gateways… — location: [3689](kindle://book?action=open&asin=B09B5L4NVT&location=3689) ^ref-3410

---
It starts off innocently enough: you combine a couple of calls and return a single payload. Then you start making another downstream call as part of the same aggregated flow. Then you start wanting to add conditional logic, and before long you realize that you’ve baked core… — location: [3692](kindle://book?action=open&asin=B09B5L4NVT&location=3692) ^ref-55466

---
Aside from the aggregation angle, protocol rewriting is also often pushed as something API… — location: [3698](kindle://book?action=open&asin=B09B5L4NVT&location=3698) ^ref-59098

---
I remember one unnamed vendor very aggressively promoting the idea that its product could “change any SOAP API into a REST API.” Firstly, REST is an entire architectural mindset that… — location: [3699](kindle://book?action=open&asin=B09B5L4NVT&location=3699) ^ref-31002

---
Secondly, protocol rewriting, which is fundamentally what this is trying to do, shouldn’t be done in intermediate layers, as it’s pushing… — location: [3700](kindle://book?action=open&asin=B09B5L4NVT&location=3700) ^ref-884

---
The main problem with both the protocol rewriting capability and the implementation of call aggregation inside API gateways is that we are violating the rule of… — location: [3702](kindle://book?action=open&asin=B09B5L4NVT&location=3702) ^ref-6655

---
It seems unlikely that individual teams will be given free rein to self-service change these often centrally managed services. What does that mean? Tickets. To roll out a change to your software, you end up having the API gateway team make changes for you. The more behavior you leak into API gateways (or into enterprise service buses)… — location: [3707](kindle://book?action=open&asin=B09B5L4NVT&location=3707) ^ref-2942

---
If we insert an API gateway or a normal network proxy between two microservices, then we have normally added at least a single network hop. A call from microservice A to microservice B first goes from A to the API gateway and then from the API gateway to B. We have to consider the latency impact of the additional network call and the overhead of whatever the proxy… — location: [3711](kindle://book?action=open&asin=B09B5L4NVT&location=3711) ^ref-65258

---
With a service mesh, common functionality associated with inter-microservice communication is pushed into the mesh. This reduces the functionality that a microservice needs to implement internally, while also… — location: [3717](kindle://book?action=open&asin=B09B5L4NVT&location=3717) ^ref-12566

---
Common features implemented by service meshes include mutual TLS, correlation IDs, service discovery… — location: [3720](kindle://book?action=open&asin=B09B5L4NVT&location=3720) ^ref-15183

---
With the use of a service mesh, though, we have the possibility of reusing common inter-microservice functionality across microservices written in different programming languages. — location: [3725](kindle://book?action=open&asin=B09B5L4NVT&location=3725) ^ref-40719

---
Service meshes can also be incredibly useful in implementing standard behavior across microservices created by different teams—and — location: [3726](kindle://book?action=open&asin=B09B5L4NVT&location=3726) ^ref-58177

---
Making it easy to implement common behavior across microservices is one of the big benefits of a service mesh. — location: [3729](kindle://book?action=open&asin=B09B5L4NVT&location=3729) ^ref-51382

---
If this common functionality was implemented solely through shared libraries, changing this behavior would require every microservice to pull in a new version of said libraries and be deployed before that change is live. With a service mesh, you have much more flexibility in rolling out changes in terms of inter-microservice communication without requiring a rebuild and redeploy. — location: [3730](kindle://book?action=open&asin=B09B5L4NVT&location=3730) ^ref-10302

---
In general, we’d expect to have less north-south traffic than east-west traffic with a microservice architecture. A single north-south call—placing an order, for example—could result in multiple east-west calls. This means that when considering any sort of proxy for in-perimeter calls, we have to be aware of the overhead these additional calls can cause, and this is a core consideration in terms of how service meshes are built. — location: [3733](kindle://book?action=open&asin=B09B5L4NVT&location=3733) ^ref-19633

---
Figure 5-7. A service mesh is deployed to handle all direct inter-microservice communication — location: [3746](kindle://book?action=open&asin=B09B5L4NVT&location=3746) ^ref-40430

---
Many service mesh implementations use the Envoy proxy for the basis of these locally running processes. Envoy is a lightweight C++ proxy often used as the building block for service meshes and other types of proxy-based software—it is an important building block for Istio and Ambassador, for example. — location: [3753](kindle://book?action=open&asin=B09B5L4NVT&location=3753) ^ref-29622

---
The key thing to remember here is that the common behavior we are putting into the mesh is not specific to any one microservice. No business functionality has leaked to the outside. We’re configuring generic things like how request time-outs are handled. — location: [3762](kindle://book?action=open&asin=B09B5L4NVT&location=3762) ^ref-46799

---
Istio, which was the Google-anointed service mesh, took years to get to an initial 1.0 release, and even still it had significant subsequent changes in its architecture (moving somewhat ironically, although sensibly, to a more monolithic deployment model for its control plane). — location: [3772](kindle://book?action=open&asin=B09B5L4NVT&location=3772) ^ref-8288

---
something like a service mesh is not where I personally want to take a lot of risks—it’s so key, so essential to everything working well. You’re putting it on your critical path. It’s up there with selecting a message broker or cloud provider in terms of how seriously I’d take it. — location: [3776](kindle://book?action=open&asin=B09B5L4NVT&location=3776) ^ref-40896

---
This means that you cannot assume your service mesh is able to work as an intermediary for all calls between microservices. — location: [3791](kindle://book?action=open&asin=B09B5L4NVT&location=3791) ^ref-63728

---
Having explicit schemas does go a long way toward making it easier to understand what any given endpoint exposes, but by themselves they are often not enough. As we’ve already discussed, schemas help show the structure, but they don’t go very far in helping communicate the behavior of an endpoint, so good documentation could still be required to help consumers understand how to use an endpoint. — location: [3803](kindle://book?action=open&asin=B09B5L4NVT&location=3803) ^ref-12168

---
Stale documentation is an ongoing problem, but at least an explicit schema gives you more chance of it being up to date. — location: [3809](kindle://book?action=open&asin=B09B5L4NVT&location=3809) ^ref-64461

---
For those on Kubernetes, Ambassador’s developer portal is especially interesting. Ambassador is already a popular choice as an API gateway for Kubernetes, and its Developer Portal has the ability to autodiscover available OpenAPI endpoints. — location: [3814](kindle://book?action=open&asin=B09B5L4NVT&location=3814) ^ref-23006

---
we should use it to harness and display all the information our system will be emitting. By creating custom dashboards, we can pull together the vast array of information that is available to help us make sense of our ecosystem. — location: [3835](kindle://book?action=open&asin=B09B5L4NVT&location=3835) ^ref-46165

---
By all means, start with something as simple as a static web page or wiki that perhaps scrapes in a bit of data from the live system. But look to pull in more and more information over time. Making this information readily available is a key tool for managing the emerging complexity that will come from running these systems at scale. — location: [3837](kindle://book?action=open&asin=B09B5L4NVT&location=3837) ^ref-53211

---
don’t fall into the trap of picking the technology first. — location: [3868](kindle://book?action=open&asin=B09B5L4NVT&location=3868) ^ref-58308

---
Whatever choice you make, consider the use of schemas, in part to help make your contracts more explicit but also to help catch accidental breaking changes. — location: [3875](kindle://book?action=open&asin=B09B5L4NVT&location=3875) ^ref-47459

---
Where possible, strive to make changes that are backward compatible to ensure that independent deployability remains a possibility. — location: [3876](kindle://book?action=open&asin=B09B5L4NVT&location=3876) ^ref-36768

---
Distributed transactions, and two-phased commits more specifically, are frequently considered by teams moving to microservice architectures as a way of solving challenges they face. But as we’ll see, they might not solve your problems and may bring even more confusion to your system. — location: [3961](kindle://book?action=open&asin=B09B5L4NVT&location=3961) ^ref-21261

---
This means that it’s possible we could see the change made to Worker A but not yet to Worker B, if we could directly observe the state of either worker. The more latency there is between the Coordinator and the participants in the two-phase commit, and the more slowly the workers process the response, the wider this window of inconsistency might be. — location: [3988](kindle://book?action=open&asin=B09B5L4NVT&location=3988) ^ref-6348

---
Managing locks and avoiding deadlocks in a single-process system isn’t fun. Now imagine the challenges of coordinating locks among multiple participants. It’s not pretty. — location: [3995](kindle://book?action=open&asin=B09B5L4NVT&location=3995) ^ref-4881

---
Some of these failure modes can be handled automatically, but some can leave the system in such a state that things need to be fixed manually by an operator. — location: [3998](kindle://book?action=open&asin=B09B5L4NVT&location=3998) ^ref-36916

---
2PC can be a quick way to inject huge amounts of latency into your system, especially if the scope of locking is large, or if the duration of the transaction is large. It’s for this reason two-phase commits are typically used only for very short-lived operations. The longer the operation takes, the longer you’ve got resources locked! — location: [4000](kindle://book?action=open&asin=B09B5L4NVT&location=4000) ^ref-8563

---
For all the reasons outlined so far, I strongly suggest you avoid the use of distributed transactions like the two-phase commit to coordinate changes in state across your microservices. So what else can you do? Well, the first option could be to just not split the data apart in the first place. — location: [4006](kindle://book?action=open&asin=B09B5L4NVT&location=4006) ^ref-49092

---
If you’re in the process of working out where to split your monolith and what decompositions might be easy (or hard), then you could well decide that splitting apart data that is currently managed in a transaction is just too difficult to handle right now. Work on some other area of the system, and come back to this later. — location: [4013](kindle://book?action=open&asin=B09B5L4NVT&location=4013) ^ref-31798

---
What Google has managed to achieve with Spanner is impressive, but it’s also worth noting that what it had to do to make this work gives you an idea of the challenges involved. Let’s just say it involves very expensive data centers and satellite-based atomic clocks (really). For a good overview of how Spanner makes this work, I recommend the presentation “Google Cloud Spanner: Global Consistency at Scale.” — location: [4024](kindle://book?action=open&asin=B09B5L4NVT&location=4024) ^ref-22064

---
a saga is by design an algorithm that can coordinate multiple changes in state, but avoids the need for locking resources for long periods of time. A saga does this by modeling the steps involved as discrete activities that can be executed independently. Using sagas comes with the added benefit of forcing us to explicitly model our business processes, which can have significant benefits. — location: [4031](kindle://book?action=open&asin=B09B5L4NVT&location=4031) ^ref-40720

---
Instead, the authors of the paper suggest we should break down these LLTs into a sequence of transactions, each of which can be handled independently. The idea is that the duration of each of these “sub” transactions will be shorter, and will modify only part of the data affected by the entire LLT. As a result, there will be far less contention in the underlying database as the scope and duration of locks is greatly reduced. — location: [4041](kindle://book?action=open&asin=B09B5L4NVT&location=4041) ^ref-32321

---
While sagas were originally envisaged as a mechanism to help with LLTs acting against a single database, the model works just as well for coordinating change across multiple services. We can break a single business process into a set of calls that will be made to collaborating services—this is what constitutes a saga. — location: [4045](kindle://book?action=open&asin=B09B5L4NVT&location=4045) ^ref-9130

---
We do have atomicity for each individual transaction inside the overall saga, as each one of them can relate to an ACID transactional change if needed. What a saga gives us is enough information to reason about which state it’s in; it’s up to us to handle the implications of this. — location: [4051](kindle://book?action=open&asin=B09B5L4NVT&location=4051) ^ref-20591

---
Backward recovery involves reverting the failure and cleaning up afterwards—a rollback. For this to work, we need to define compensating actions that allow us to undo previously committed transactions. — location: [4067](kindle://book?action=open&asin=B09B5L4NVT&location=4067) ^ref-11931

---
Forward recovery allows us to pick up from the point where the failure occurred and keep processing. For that to work, we need to be able to retry transactions, which in turn implies that our system is persisting enough information to allow this retry to take place. — location: [4069](kindle://book?action=open&asin=B09B5L4NVT&location=4069) ^ref-4247

---
Depending on the nature of the business process being modeled, you may expect that any failure mode triggers a backward recovery, a forward recovery, or perhaps a mix of the two. — location: [4071](kindle://book?action=open&asin=B09B5L4NVT&location=4071) ^ref-35663

---
The saga assumes the underlying components are working properly—that the underlying system is reliable, and that we are then coordinating the work of reliable components. — location: [4077](kindle://book?action=open&asin=B09B5L4NVT&location=4077) ^ref-13800

---
Instead, if you want to implement a rollback, you need to implement a compensating transaction. A compensating transaction is an operation that undoes a previously committed transaction. — location: [4096](kindle://book?action=open&asin=B09B5L4NVT&location=4096) ^ref-54288

---
Because we cannot always cleanly revert a transaction, we say that these compensating transactions are semantic rollbacks. We cannot always clean up everything, but we do enough for the context of our saga. — location: [4106](kindle://book?action=open&asin=B09B5L4NVT&location=4106) ^ref-46749

---
It is totally appropriate for information related to the rollback to persist in the system. In fact, this may be very important information. You may want to keep a record in the Order service for this aborted order, along with information about what happened, for a whole host of reasons. — location: [4112](kindle://book?action=open&asin=B09B5L4NVT&location=4112) ^ref-9519

---
Mixing fail-backward and fail-forward situations It is totally appropriate to have a mix of failure recovery modes. Some failures may require a rollback (fail backward); others may be fail forward. — location: [4129](kindle://book?action=open&asin=B09B5L4NVT&location=4129) ^ref-19096

---
Orchestrated sagas more closely follow the original solution space and rely primarily on centralized coordination and tracking. These can be compared to choreographed sagas, which avoid the need for centralized coordination in favor of a more loosely coupled model but can make tracking the progress of a saga more complicated. — location: [4139](kindle://book?action=open&asin=B09B5L4NVT&location=4139) ^ref-64004

---
If the calls fail, it can decide what to do as a result. In general, orchestrated sagas tend to make heavy use of request-response interactions between services: — location: [4153](kindle://book?action=open&asin=B09B5L4NVT&location=4153) ^ref-49629

---
Having our business process explicitly modeled inside the Order Processor is extremely beneficial. It allows us to look at one place in our system and understand how this process is supposed to work. That can make the onboarding of new people easier and help impart a better understanding of the core parts of the system. There are a few downsides to consider, though. First, by its nature, this is a somewhat coupled approach. — location: [4157](kindle://book?action=open&asin=B09B5L4NVT&location=4157) ^ref-19087

---
While domain coupling is not inherently bad, we’d still like to keep it to a minimum, if possible. — location: [4161](kindle://book?action=open&asin=B09B5L4NVT&location=4161) ^ref-40752

---
The other issue, which is more subtle, is that logic that should otherwise be pushed into the services can start to become absorbed in the orchestrator instead. If this begins to happen, you may find that your services become anemic, with little behavior of their own, just taking orders from orchestrators — location: [4163](kindle://book?action=open&asin=B09B5L4NVT&location=4163) ^ref-19524

---
It’s important you still consider the services that make up these orchestrated flows as entities that have their own local state and behavior. They are in charge of their own local state machines. — location: [4166](kindle://book?action=open&asin=B09B5L4NVT&location=4166) ^ref-25193

---
Warning If logic has a place where it can be centralized, it will become centralized! One way to avoid too much centralization with orchestrated flows is to ensure you have different services playing the role of the orchestrator for different flows. — location: [4168](kindle://book?action=open&asin=B09B5L4NVT&location=4168) ^ref-19832

---
The use of such tools seems to line up really nicely as a way of implementing orchestrated sagas, and indeed, process orchestration is pretty much the main use case for BPM tools (or, in reverse, the use of BPM tools results in you having to adopt orchestration). — location: [4181](kindle://book?action=open&asin=B09B5L4NVT&location=4181) ^ref-39500

---
In my experience, I’ve come to greatly dislike BPM tools. The main reason is that the central conceit—that nondevelopers will define the business process—has in my experience almost never been true. — location: [4183](kindle://book?action=open&asin=B09B5L4NVT&location=4183) ^ref-51891

---
The tooling aimed at nondevelopers ends up getting used by developers, and unfortunately these tools often work in ways that are alien to how developers like to work. — location: [4184](kindle://book?action=open&asin=B09B5L4NVT&location=4184) ^ref-43026

---
There are efforts to create more developer-friendly BPM tools. Feedback on these tools from developers seems to be mixed, but the tools have worked well for some, and it’s good to see people trying to improve on these frameworks. If you feel the need to explore these tools further, do take a look at Camunda and Zeebe, both of which are open source orchestration frameworks targeting microservice developers, and which would be at the top of my list if I decided that a BPM tool was for me. — location: [4190](kindle://book?action=open&asin=B09B5L4NVT&location=4190) ^ref-51444

---
A choreographed saga aims to distribute responsibility for the operation of the saga among multiple collaborating services. If orchestration is a command-and-control approach, choreographed sagas represent a trust-but-verify architecture. — location: [4197](kindle://book?action=open&asin=B09B5L4NVT&location=4197) ^ref-53058

---
First, these microservices are reacting to events being received. Conceptually, events are broadcast in the system, and interested parties are able to receive them. Remember, as we discussed in Chapter 4, you don’t send events to a microservice; you just fire them out, and the microservices that are interested in these events are able to receive them and act accordingly. — location: [4204](kindle://book?action=open&asin=B09B5L4NVT&location=4204) ^ref-42727

---
We also see in this example how events can facilitate parallel processing. — location: [4211](kindle://book?action=open&asin=B09B5L4NVT&location=4211) ^ref-8353

---
Typically, you’d use some sort of message broker to manage the reliable broadcast and delivery of events. It’s possible that multiple microservices may react to the same event, and that is where you would use a topic. Parties interested in a certain type of event would subscribe to a specific topic without having to worry about where these events came from, and the broker ensures the durability of the topic and that the events on it are successfully delivered to subscribers. — location: [4215](kindle://book?action=open&asin=B09B5L4NVT&location=4215) ^ref-44248

---
In the preceding architecture, no one service knows about any other microservice. They need to know only what to do when a certain event is received—we’ve drastically reduced the amount of domain coupling. Inherently, this makes for a much less coupled architecture. — location: [4221](kindle://book?action=open&asin=B09B5L4NVT&location=4221) ^ref-51473

---
As the implementation of the process is decomposed and distributed among the three microservices here, we also avoid the concerns about centralization of logic (if you don’t have a place where logic can be centralized, then it won’t be centralized!). — location: [4223](kindle://book?action=open&asin=B09B5L4NVT&location=4223) ^ref-10000

---
You’d have to look at the behavior of each service in isolation and reconstitute this picture in your own head—far from straightforward, even with a simple business process like this one. — location: [4226](kindle://book?action=open&asin=B09B5L4NVT&location=4226) ^ref-36345

---
fundamentally we need a way of knowing what state a saga is in for some kinds of recovery. The lack of a central place to interrogate around the status of a saga is a big problem. — location: [4230](kindle://book?action=open&asin=B09B5L4NVT&location=4230) ^ref-62064

---
One of the easiest ways of doing this is to project a view regarding the state of a saga by consuming the events being emitted. If we generate a unique ID for the saga, what is known as a correlation ID, we can put it into all of the events that are emitted as part of this saga. When one of our services reacts to an event, the correlation ID is extracted and used for any local logging processes, and it’s also passed downstream with any further calls or events that are fired. We could then have a service whose job it is to just vacuum up all these events and present a view of what state each order is in, and perhaps programmatically carry out actions to resolve issues as part of the fulfillment process if the other services couldn’t do it themselves. — location: [4232](kindle://book?action=open&asin=B09B5L4NVT&location=4232) ^ref-8563

---
You may have some business processes in your system that more naturally fit one model or another. You may also have a single saga that has a mix of styles. — location: [4242](kindle://book?action=open&asin=B09B5L4NVT&location=4242) ^ref-61937

---
If you do decide to mix styles, it’s important that you still have a clear way to understand what state a saga is in, and what activities have already happened as part of a saga. Without this, understanding failure modes becomes complex, and recovery from failure is difficult. — location: [4246](kindle://book?action=open&asin=B09B5L4NVT&location=4246) ^ref-24593

---
Whether you chose choreography or orchestration, when implementing a business process using multiple microservices, it’s common to want to be able to trace all the calls related to the process. This can sometimes be just to help you understand if the business process is working correctly, or it could be to help you diagnose a problem. — location: [4250](kindle://book?action=open&asin=B09B5L4NVT&location=4250) ^ref-64152

---
The implementation of choreographed sagas can bring with it ideas that may be unfamiliar to you and your team. They typically assume heavy use of event-driven collaboration, which isn’t widely understood. — location: [4256](kindle://book?action=open&asin=B09B5L4NVT&location=4256) ^ref-3825

---
However, in my experience, the extra complexity associated with tracking the progress of a saga is almost always outweighed by the benefits associated with having a more loosely coupled architecture. — location: [4257](kindle://book?action=open&asin=B09B5L4NVT&location=4257) ^ref-15808

---
Stepping aside from my own personal tastes, though, the general advice I give regarding orchestration versus choreography is that I am very relaxed in the use of orchestrated sagas when one team owns implementation of the entire saga. In such a situation, the more inherently coupled architecture is much easier to manage within the team boundary. — location: [4258](kindle://book?action=open&asin=B09B5L4NVT&location=4258) ^ref-12302

---
If you have multiple teams involved, I greatly prefer the more decomposed choreographed saga, as it is easier to distribute responsibility for implementing the saga to the teams, with the more loosely coupled architecture allowing these teams to work more in isolation. — location: [4261](kindle://book?action=open&asin=B09B5L4NVT&location=4261) ^ref-5553

---
It’s worth noting that as a general rule, you’ll be more likely to gravitate toward request-response–based calls with orchestration, whereas choreography tends to make heavier use of events. — location: [4263](kindle://book?action=open&asin=B09B5L4NVT&location=4263) ^ref-8008

---
if you are finding the use of event-driven collaboration difficult to get your head around, choreography might not be for you. — location: [4265](kindle://book?action=open&asin=B09B5L4NVT&location=4265) ^ref-18837

---
In most distributed transaction systems, the failure of a single node causes transaction commit to stall. This in turn causes the application to get wedged. In such systems, the larger it gets, the more likely the system is going to be down. When flying an airplane that needs all of its engines to work, adding an engine reduces the availability of the airplane. — location: [4276](kindle://book?action=open&asin=B09B5L4NVT&location=4276) ^ref-39943

---
In my experience, explicitly modeling business processes as a saga avoids many of the challenges of distributed transactions, while having the added benefit of making what might otherwise be implicitly modeled processes much more explicit and obvious to your developers. Making the core business processes of your system a first-class concept will have a host of advantages. — location: [4279](kindle://book?action=open&asin=B09B5L4NVT&location=4279) ^ref-3858

---
If you want to explore this space in more detail, although sagas aren’t explicitly covered, Enterprise Integration Patterns by Gregor Hohpe and Bobby Woolf has a number of patterns that can be incredibly useful when implementing different types of workflow.8 I can also heartily recommend Practical Process Automation by Bernd Ruecker.9 Bernd’s book focuses much more on the orchestration side of sagas, but it is packed with useful information that makes it a natural following-on point for this topic. — location: [4288](kindle://book?action=open&asin=B09B5L4NVT&location=4288) ^ref-3202

---
So how do you know if you’re actually practicing CI? I really like Jez Humble’s three questions he asks people to test if they really understand what CI is about—it might be interesting to ask yourself these same questions: — location: [4350](kindle://book?action=open&asin=B09B5L4NVT&location=4350) ^ref-58070

---
Do you check in to mainline once per day? You need to make sure your code integrates. If you don’t check your code together with everyone else’s changes frequently, you end up making future integration harder. Even if you are using short-lived branches to manage changes, integrate as frequently as you can into a single mainline branch—at least once a day. — location: [4352](kindle://book?action=open&asin=B09B5L4NVT&location=4352) ^ref-61424

---
Do you have a suite of tests to validate your changes? Without tests, we just know that syntactically our integration has worked, but we don’t know if we have broken the behavior of the system. CI without some verification that our code behaves as expected isn’t CI. — location: [4355](kindle://book?action=open&asin=B09B5L4NVT&location=4355) ^ref-62567

---
When the build is broken, is it the #1 priority of the team to fix it? A passing green build means our changes have safely been integrated. A red build means the last change possibly did not integrate. You need to stop all further check-ins that aren’t involved in fixing the builds to get it passing again. If you let more changes pile up, the time it takes to fix the build will increase drastically. — location: [4357](kindle://book?action=open&asin=B09B5L4NVT&location=4357) ^ref-2473

---
The problem is that when you work on a feature branch, you aren’t regularly integrating your changes with everyone else. Fundamentally, you are delaying integration. And when you finally decide to integrate your changes with everyone else, you’ll have a much more complex merge. — location: [4369](kindle://book?action=open&asin=B09B5L4NVT&location=4369) ^ref-50854

---
The alternative approach is to have everyone check in to the same “trunk” of source code. To keep changes from impacting other people, techniques like feature flags are used to “hide” incomplete work. This technique of everyone working off the same trunk is called trunk-based development. — location: [4371](kindle://book?action=open&asin=B09B5L4NVT&location=4371) ^ref-22166

---
The discussion around this topic is nuanced, but my own take is that the benefits of frequent integration—and validation of that integration—are significant enough that trunk-based development is my preferred style of development. Moreover, the work to implement feature flags is frequently beneficial in terms of progressive delivery, a concept we’ll explore in Chapter 8. — location: [4374](kindle://book?action=open&asin=B09B5L4NVT&location=4374) ^ref-9225

---
We found that having branches or forks with very short lifetimes (less than a day) before being merged into trunk, and less than three active branches in total, are important aspects of continuous delivery, and all contribute to higher performance. So does merging code into trunk or master on a daily basis. — location: [4384](kindle://book?action=open&asin=B09B5L4NVT&location=4384) ^ref-9260

---
The State of DevOps report has continued to explore this topic in more depth in subsequent years, and has continued to find evidence for the efficacy of this approach. — location: [4387](kindle://book?action=open&asin=B09B5L4NVT&location=4387) ^ref-37054

---
Open source development is characterized by a large number of ad hoc contributions from time-poor “untrusted” committers, whose changes require vetting by a smaller number of “trusted” contributors. — location: [4391](kindle://book?action=open&asin=B09B5L4NVT&location=4391) ^ref-35740

---
Typical day-to-day closed source development is normally done by a tight-knit team whose members all have commit rights, even if they decide to adopt some form of code review process. — location: [4393](kindle://book?action=open&asin=B09B5L4NVT&location=4393) ^ref-3185

---
So what might work for open source development may not work for your day job. — location: [4394](kindle://book?action=open&asin=B09B5L4NVT&location=4394) ^ref-38547

---
Our research findings extend to open source development in some areas: Committing code sooner is better: In open source projects, many have observed that merging patches faster to prevent rebases helps developers move faster. Working in small batches is better: Large “patch bombs” are harder and slower to merge into a project than smaller, more readable patchsets since maintainers need more time to review the changes. — location: [4399](kindle://book?action=open&asin=B09B5L4NVT&location=4399) ^ref-36808

---
Whether you are working on a closed-source code base or an open source project, short-lived branches; small, readable patches; and automatic testing of changes make everyone more productive. — location: [4402](kindle://book?action=open&asin=B09B5L4NVT&location=4402) ^ref-14678

---
Continuous delivery (CD) builds on this concept, and then some. As outlined in Jez Humble and Dave Farley’s book of the same name,3 CD is the approach whereby we get constant feedback on the production readiness of each and every check-in, and furthermore treat each and every check-in as a release candidate. — location: [4422](kindle://book?action=open&asin=B09B5L4NVT&location=4422) ^ref-23896

---
To fully embrace this concept, we need to model all the processes involved in getting our software from check-in to production, and we need to know where any given version of the software is in terms of being cleared for release. — location: [4427](kindle://book?action=open&asin=B09B5L4NVT&location=4427) ^ref-26857

---
continuous delivery is the concept whereby each check-in is treated as a release candidate, and whereby we can assess the quality of each release candidate to decide if it’s ready to be deployed. — location: [4445](kindle://book?action=open&asin=B09B5L4NVT&location=4445) ^ref-9678

---
With continuous deployment on the other hand, all check-ins have to be validated using automated mechanisms (tests for example), and any software that passes these verification checks is deployed automatically, without human intervention. — location: [4446](kindle://book?action=open&asin=B09B5L4NVT&location=4446) ^ref-16477

---
Continuous deployment can therefore be considered an extention of continuous delivery. Without continuous delivery, you can’t do continuous deployment. — location: [4448](kindle://book?action=open&asin=B09B5L4NVT&location=4448) ^ref-61677

---
Continuous deployment isn’t right for everyone—many people want some human interaction to decide whether software should be deployed, something that is totally compatible with continuous delivery. — location: [4450](kindle://book?action=open&asin=B09B5L4NVT&location=4450) ^ref-65164

---
Often human involvement in the post-check-in process is a bottleneck that needs addressing—see — location: [4453](kindle://book?action=open&asin=B09B5L4NVT&location=4453) ^ref-12316

---
As a result, as you automate more and more of your build, deployment, and release process, you may find yourself getting closer and closer to continuous deployment. — location: [4454](kindle://book?action=open&asin=B09B5L4NVT&location=4454) ^ref-38094

---
Tools that fully support CD allow you to define and visualize these pipelines, modeling the entire path to production for your software. — location: [4461](kindle://book?action=open&asin=B09B5L4NVT&location=4461) ^ref-38217

---
Some stages may be manual. — location: [4463](kindle://book?action=open&asin=B09B5L4NVT&location=4463) ^ref-31870

---
If the subsequent stage is automated, it will then get triggered automatically. — location: [4465](kindle://book?action=open&asin=B09B5L4NVT&location=4465) ^ref-39076

---
Structuring a pipeline, and therefore working out what environments you’ll need, is in and of itself a balancing act. Early on in the pipeline, we’re looking for fast feedback on the production readiness of our software. — location: [4471](kindle://book?action=open&asin=B09B5L4NVT&location=4471) ^ref-29795

---
You get the fastest feedback on your development laptop—but that is far from production-like. You could roll out every commit to an environment that is a faithful reproduction of your actual production environment, but that will likely take longer and cost more. So finding the balance is key, and continuing to review the trade-off between fast feedback and the need for production-like environments can be an incredibly important ongoing activity. — location: [4478](kindle://book?action=open&asin=B09B5L4NVT&location=4478) ^ref-11527

---
The challenges of creating a production-like environment are also part of why more people are doing forms of testing in production, including techniques such as smoke testing and parallel runs. — location: [4482](kindle://book?action=open&asin=B09B5L4NVT&location=4482) ^ref-18480

---
Now, there are two important rules we need to consider. Firstly, as I mentioned earlier, we should build an artifact once and once only. Building the same thing over and over again is a waste of time and bad for the planet, and it can theoretically introduce problems if the build configuration isn’t exactly the same each time. — location: [4491](kindle://book?action=open&asin=B09B5L4NVT&location=4491) ^ref-45558

---
Taking these two ideas together, we have a pretty simple approach. Build your deployable artifact once and once only, and ideally do it pretty early in the pipeline. — location: [4496](kindle://book?action=open&asin=B09B5L4NVT&location=4496) ^ref-25489

---
Once created, this artifact is stored in an appropriate repository—this could be something like Artifactory or Nexus, or perhaps a container registry. Your choice of deployment artifact likely dictates the nature of the artifact store. — location: [4498](kindle://book?action=open&asin=B09B5L4NVT&location=4498) ^ref-64752

---
This same artifact can then be used for all stages in the pipeline that follow, up to and including deployment into production. — location: [4499](kindle://book?action=open&asin=B09B5L4NVT&location=4499) ^ref-51936

---
If the same artifact is going to be used across multiple environments, any aspects of configuration that vary from environment to environment need to be kept outside the artifact itself. — location: [4506](kindle://book?action=open&asin=B09B5L4NVT&location=4506) ^ref-57270

---
Build a deployment artifact for your microservice once. Reuse this artifact everywhere you want to deploy that version of your microservice. Keep your deployment artifact environment-agnostic—store environment-specific configuration elsewhere. — location: [4511](kindle://book?action=open&asin=B09B5L4NVT&location=4511) ^ref-35152

---
This model can work perfectly well if you buy into the idea of lockstep releases, where you don’t mind deploying multiple services at once. In general, this is absolutely a pattern to avoid, but very early on in a project, especially if only one team is working on everything, this model might make sense for short periods of time. — location: [4529](kindle://book?action=open&asin=B09B5L4NVT&location=4529) ^ref-17406

---
Arguably, this approach is a form of monorepo. In practice, however, most of the monorepo implementations I’ve seen map multiple builds to different parts of the repo, something we’ll explore in more depth shortly. — location: [4541](kindle://book?action=open&asin=B09B5L4NVT&location=4541) ^ref-57514

---
The straightforward nature of this pattern does create some challenges, however. Specifically, developers may find themselves working with multiple repositories at a time, which is especially painful if they are trying to make changes across multiple repositories at once. Additionally, changes cannot be made in an atomic fashion across separate repositories, at least not with Git. — location: [4559](kindle://book?action=open&asin=B09B5L4NVT&location=4559) ^ref-43623

---
Remember, all the caveats we explored in “DRY and the Perils of Code Reuse in a Microservice World” regarding reuse and microservices still apply—if you choose to reuse code via libraries, then you must be OK with the fact that these changes cannot be rolled out in an atomic fashion, or else we undermine our goal of independent deployability. — location: [4581](kindle://book?action=open&asin=B09B5L4NVT&location=4581) ^ref-49288

---
You also have to be aware that it can be more challenging to know if some microservices are using a specific version of a library, which may be problematic if you’re trying to deprecate the use of an old version of the library. — location: [4583](kindle://book?action=open&asin=B09B5L4NVT&location=4583) ^ref-27975

---
I’ve spoken to multiple people who find the lack of atomic deployment with this to be a significant problem. I can certainly appreciate the complexity this brings, but I think that in most cases it points to a bigger underlying issue. If you are continually making changes across multiple microservices, then your service boundaries might not be in the right place, and it could imply too much coupling between your services. — location: [4600](kindle://book?action=open&asin=B09B5L4NVT&location=4600) ^ref-58162

---
As we’ve already discussed, we’re trying to optimize our architecture, and our microservice boundaries, so that changes are more likely going to apply within a microservice boundary. Cross-cutting changes should be the exception, not the norm. — location: [4603](kindle://book?action=open&asin=B09B5L4NVT&location=4603) ^ref-25843

---
In fact, I’d argue that the pain of working across multiple repos can be useful in helping enforce microservice boundaries, as it forces you to think carefully about where these boundaries are, and about the nature of the interactions between them. — location: [4605](kindle://book?action=open&asin=B09B5L4NVT&location=4605) ^ref-64318

---
I have seen situations in which a monorepo is used just by one team to manage source control for all its services, although the concept has been popularized by some very large tech companies where multiple teams and hundreds if not thousands of developers can all work on the same source code repository. — location: [4623](kindle://book?action=open&asin=B09B5L4NVT&location=4623) ^ref-44735

---
Google is probably the best-known example of a company using a monorepo approach, although it’s far from the only one. — location: [4626](kindle://book?action=open&asin=B09B5L4NVT&location=4626) ^ref-31002

---
Although there are some other benefits to this approach, such as improved visibility of other people’s code, the ability to reuse code easily and to make changes that impact multiple different projects is often cited as the major reason for adopting this pattern. — location: [4627](kindle://book?action=open&asin=B09B5L4NVT&location=4627) ^ref-52553

---
With a multirepo model, if I want to reuse someone else’s code, it will likely have to be packaged as a versioned artifact that I can then include as part of my build (such as a Nuget package, a JAR file, or an NPM). — location: [4660](kindle://book?action=open&asin=B09B5L4NVT&location=4660) ^ref-4800

---
Theoretically, with a monorepo I could just depend on a single source file from another project—although this of course will cause me to have a more complex build mapping. — location: [4662](kindle://book?action=open&asin=B09B5L4NVT&location=4662) ^ref-64508

---
With strong ownership, some code is owned by a specific group of people. If someone from outside that group wants to make a change, they have to ask the owners to make the change for them. — location: [4671](kindle://book?action=open&asin=B09B5L4NVT&location=4671) ^ref-26150

---
Weak ownership still has the concept of defined owners, but people outside the ownership group are allowed to make changes, although any of these changes must be reviewed and accepted by someone in the ownership group. This would cover a pull request being sent to the core ownership team for review, before the pull request is merged. — location: [4673](kindle://book?action=open&asin=B09B5L4NVT&location=4673) ^ref-54494

---
With collective ownership, any developer can change any piece of code. — location: [4675](kindle://book?action=open&asin=B09B5L4NVT&location=4675) ^ref-39388

---
As you have more people, though, you’re more likely to want to move toward either a strong or weak ownership model to create more defined boundaries of responsibility. — location: [4677](kindle://book?action=open&asin=B09B5L4NVT&location=4677) ^ref-54471

---
Some source code tools allow you to specify ownership of specific directories or even specific filepaths inside a single repository. Google initially implemented this system on top of Perforce for its own monorepo before developing its own source control system, and it’s also something that GitHub has supported since 2016. With GitHub, you create a CODEOWNERS file, which lets you map owners to directories or filepaths. — location: [4679](kindle://book?action=open&asin=B09B5L4NVT&location=4679) ^ref-30499

---
Google’s own monorepo is massive, and it takes significant amounts of engineering to make it work at scale. Consider things like a graph-based build system that has gone through multiple generations, a distributed object linker to speed up build times, plug-ins for IDEs and text editors that can dynamically keep dependency files in check—it’s an enormous amount of work. — location: [4694](kindle://book?action=open&asin=B09B5L4NVT&location=4694) ^ref-52925

---
I’ve also spoken to teams that practice per-team monorepos. While technically speaking this probably doesn’t match up to the original definition of this pattern (which typically talks in terms of multiple teams sharing the same repository), I still think it’s more “monorepo” than anything else. In this situation, each team has its own monorepo that is fully under its control. All microservices owned by that team have their code stored in that team’s monorepo, — location: [4724](kindle://book?action=open&asin=B09B5L4NVT&location=4724) ^ref-42470

---
For teams practicing collective ownership, this model has a lot of benefits, arguably providing most of the advantages of a monorepo approach while sidestepping some of the challenges that occur at larger scale. This halfway house can make a lot of sense in terms of working within existing organizational ownership boundaries, and it can somewhat mitigate the concerns about the use of this pattern at larger scale. — location: [4730](kindle://book?action=open&asin=B09B5L4NVT&location=4730) ^ref-20618

---
Where I see monorepos work well is at the other end of the spectrum, with smaller numbers of developers and teams. With 10 to 20 developers, it is easier to manage ownership boundaries and keep the build process simple with the monorepo approach. — location: [4737](kindle://book?action=open&asin=B09B5L4NVT&location=4737) ^ref-40142

---
A problem I’ve seen repeatedly is that organizations that started small, where collective ownership (and therefore monorepos) worked well initially, have struggled to move to different models later on, as the concept of the monorepo is so ingrained. As the delivery organization grows, the pain of the monorepo increases, but so too does the cost of migrating to an alternative approach. — location: [4746](kindle://book?action=open&asin=B09B5L4NVT&location=4746) ^ref-835

---
This is even more challenging for organizations that grew rapidly, as it’s often only after that rapid growth has occurred that the problems become evident, at which point the cost of migration to a multirepo approach looks too high. This can lead to the sunk cost fallacy: you’ve invested so much in making the monorepo work up to this point—just a bit more investment will make it work as well as it used to, right? Perhaps not—but it’s a brave soul who can recognize that they are throwing good money after bad and make a decision to change course. — location: [4749](kindle://book?action=open&asin=B09B5L4NVT&location=4749) ^ref-22133

---
My opinion on this might change as the maturity of tooling around monorepos improves, but despite a lot of work being done in regard to the open source development of graph-based build tools, I’m still seeing very low take-up of these toolchains. So it’s multirepos for me. — location: [4754](kindle://book?action=open&asin=B09B5L4NVT&location=4754) ^ref-24555

---
When it comes to something like a managed virtual machine, neither AWS nor Azure nor Google will give you an SLA for a single machine, nor do they give you an SLA for a single availability zone (which is the closest equivalent to a data center for these providers). In practice, this means that any solution you deploy should be distributed across multiple availability zones. — location: [4818](kindle://book?action=open&asin=B09B5L4NVT&location=4818) ^ref-11343

---
Broadly speaking, a physical database deployment might be hosted on multiple machines, for a host of reasons. A common example would be to split load for reads and writes between a primary node and one or more nodes that are designated for read-only purposes (these nodes are typically referred to as read replicas). — location: [4842](kindle://book?action=open&asin=B09B5L4NVT&location=4842) ^ref-39132

---
The important thing to realize here is that although these two databases might be run from the same hardware and database engine, they are still logically isolated databases. They cannot interfere with each other (unless you allow that). — location: [4859](kindle://book?action=open&asin=B09B5L4NVT&location=4859) ^ref-19082

---
The one major thing to consider is that if this shared database infrastructure fails, you might impact multiple microservices, which could have catastrophic impact. — location: [4860](kindle://book?action=open&asin=B09B5L4NVT&location=4860) ^ref-37266

---
Provisioning and managing hardware is painful (and historically at least, databases are less likely to run on virtualized infrastructure), so you want less of that. — location: [4863](kindle://book?action=open&asin=B09B5L4NVT&location=4863) ^ref-14881

---
On the other hand, teams that run on public cloud providers are much more likely to provision dedicated database infrastructure on a per-microservice basis, as shown in Figure 8-7. The costs of provisioning and managing this infrastructure are much lower. AWS’s Relational Database Service (RDS), for example, can automatically handle concerns like backups, upgrades, and multiavailability zone failover, and similar products are available from the other public cloud providers. This makes it much more cost effective to have more isolated infrastructure for your microservice, giving each microservice owner more control rather than having to rely on a shared service. — location: [4865](kindle://book?action=open&asin=B09B5L4NVT&location=4865) ^ref-38326

---
Typically, we think of our software as moving through a number of preproduction environments, with each one serving some purpose to allow the software to be developed and its readiness for production to be tested—we — location: [4881](kindle://book?action=open&asin=B09B5L4NVT&location=4881) ^ref-35938

---
From a developer laptop to a continuous integration server, an integrated test environment, and beyond—the exact nature and number of your environments will depend on a host of factors but will be driven primarily by how you choose to develop software. — location: [4883](kindle://book?action=open&asin=B09B5L4NVT&location=4883) ^ref-19459

---
Ideally, each environment in this process would be an exact copy of the production environment. This would give us even more confidence that our software will work when it reaches production. However, in reality, we often can’t afford to run multiple copies of our entire production environment due to how expensive this is. — location: [4893](kindle://book?action=open&asin=B09B5L4NVT&location=4893) ^ref-53617

---
We also want to tune environments earlier in this process to allow for fast feedback. It’s vital that we know as early as possible whether or not our software works so that we can fix things quickly, if needed. The earlier we know about a problem with our software, the faster it is to fix it, and the lower the impact of the break. — location: [4896](kindle://book?action=open&asin=B09B5L4NVT&location=4896) ^ref-55121

---
This means that environments closer to the developer will be tuned to provide fast feedback, which may compromise how “production-like” they are. But as environments get closer to production, we will want them to be more and more like the end production environment to ensure that we catch problems. — location: [4901](kindle://book?action=open&asin=B09B5L4NVT&location=4901) ^ref-4467

---
As a simple example of this in action, let’s revisit our earlier example of the Catalog service and take a look at the different environments. In Figure 8-9, the local developer laptop has our service deployed as a single instance running locally. The software is fast to build but is deployed as a single instance running on very different hardware from what we expect in production. In the CI environment, we deploy two copies of our service to test against, making sure our load balancing logic is working OK. We deploy both instances to the same machine—this keeps costs down and makes things faster, and it still gives us enough feedback at this stage in the process. — location: [4903](kindle://book?action=open&asin=B09B5L4NVT&location=4903) ^ref-64407

---
Finally, in production, our microservice is deployed as four instances, spread across four machines, which in turn are distributed across two different data centers. — location: [4911](kindle://book?action=open&asin=B09B5L4NVT&location=4911) ^ref-19129

---
This is just an example of how you might use environments; exactly what setup you’ll need will vary greatly depending on what you are building and how you deploy it. You might, for example, have multiple production environments if you need to deploy one copy of your software for each customer. — location: [4912](kindle://book?action=open&asin=B09B5L4NVT&location=4912) ^ref-35837

---
The key thing, though, is that the exact topology of your microservice will change from environment to environment. You therefore need to find ways to change the number of instances from one environment to another, along with any environment-specific configuration. — location: [4914](kindle://book?action=open&asin=B09B5L4NVT&location=4914) ^ref-4973

---
You also want to build your service instances once and once only, so it follows that any environment-specific information needs to be separate from the deployed service artifact. — location: [4916](kindle://book?action=open&asin=B09B5L4NVT&location=4916) ^ref-22432

---
Isolated execution Run microservice instances in an isolated fashion such that they have their own computing resources, and their execution cannot impact other microservice instances running nearby. — location: [4929](kindle://book?action=open&asin=B09B5L4NVT&location=4929) ^ref-40343

---
Focus on automation As the number of microservices increases, automation becomes increasingly important. Focus on choosing technology that allows for a high degree of automation, and adopt automation as a core part of your culture. — location: [4930](kindle://book?action=open&asin=B09B5L4NVT&location=4930) ^ref-62628

---
Infrastructure as code Represent the configuration for your infrastructure to ease automation and promote information sharing. Store this code in source control to allow for environments to be re-created. — location: [4933](kindle://book?action=open&asin=B09B5L4NVT&location=4933) ^ref-53934

---
Zero-downtime deployment Take independent deployability further and ensure that deploying a new version of a microservice can be done without any downtime to users of your service (be they humans or other microservices). — location: [4934](kindle://book?action=open&asin=B09B5L4NVT&location=4934) ^ref-16609

---
Desired state management Use a platform that maintains your microservice in a defined state, launching new instances if required in the event of outages or traffic increases. — location: [4937](kindle://book?action=open&asin=B09B5L4NVT&location=4937) ^ref-63234

---
Deployment of services can be somewhat more complex too, as ensuring one deployment doesn’t affect another leads to additional headaches. For example, if each microservice has different (and potentially contradictory) dependencies that need to be installed on the shared host, how can I make that work? — location: [4954](kindle://book?action=open&asin=B09B5L4NVT&location=4954) ^ref-19796

---
Fundamentally, running lots of microservice instances on the same machine (virtual or physical) ends up drastically undermining one of the key principles of microservices as a whole—independent deployability. — location: [4959](kindle://book?action=open&asin=B09B5L4NVT&location=4959) ^ref-52835

---
In general, the isolation around containers has improved sufficiently to make them a more natural choice for microservice workloads. The difference in isolation between containers and VMs has reduced to the point that for the vast majority of workloads, containers are “good enough,” which is in large part why they are such a popular choice and why they tend to be my default choice in most situations. — location: [4980](kindle://book?action=open&asin=B09B5L4NVT&location=4980) ^ref-59523

---
Focus on Automation As you add more microservices, you’ll have more moving parts to deal with—more processes, more things to configure, more instances to monitor. Moving to microservices pushes a lot of complexity into the operational space, and if you are managing your operational processes in a mostly manual way, this means that more services will require more and more people to do things. — location: [4984](kindle://book?action=open&asin=B09B5L4NVT&location=4984) ^ref-58159

---
Picking technology that enables automation starts with the tools used to manage hosts. Can you write a line of code to launch a virtual machine, or shut one down? Can you deploy the software you have written automatically? Can you deploy database changes without manual intervention? Embracing a culture of automation is key if you want to keep the complexities of microservice architectures in check. — location: [4994](kindle://book?action=open&asin=B09B5L4NVT&location=4994) ^ref-43417

---
Version controlling your infrastructure code gives you transparency over who has made changes, something that auditors love. It also makes it easier to reproduce an environment at a given point in time. — location: [5029](kindle://book?action=open&asin=B09B5L4NVT&location=5029) ^ref-50396

---
Implementing the ability for zero-downtime deployment can be a huge step up in allowing microservices to be developed and deployed. Without zero-downtime deployment, I may have to coordinate with upstream consumers when I release software to alert them of a potential outage. — location: [5043](kindle://book?action=open&asin=B09B5L4NVT&location=5043) ^ref-11539

---
In addition, a zero-downtime release can be much more easily done during working hours. Quite aside from the fact that doing so improves the quality of life of the people involved with the release (compared to working evenings and weekends), a well-rested team working during the day is less likely to make mistakes and will have support from many of their colleagues when they need to fix issues. — location: [5047](kindle://book?action=open&asin=B09B5L4NVT&location=5047) ^ref-22512

---
If you’re making use of synchronous-based communication, though, this can be more problematic. Concepts like rolling upgrades can be handy here, and this is one area where the use of a platform like Kubernetes makes your life much easier. — location: [5053](kindle://book?action=open&asin=B09B5L4NVT&location=5053) ^ref-31217

---
With a rolling upgrade, your microservice isn’t totally shut down before the new version is deployed, instead instances of your microservice are slowly ramped down as new instances running new versions of your software are ramped up. — location: [5054](kindle://book?action=open&asin=B09B5L4NVT&location=5054) ^ref-7786

---
Whether or not you are able to implement a zero-downtime deployment for your services initially, if you can get there you’ll certainly appreciate that increased level of independence. — location: [5061](kindle://book?action=open&asin=B09B5L4NVT&location=5061) ^ref-54076

---
The beauty of desired state management is that the platform itself manages how the desired state is maintained. It frees development and operations people alike from having to worry about exactly how things are being done—they just have to focus on getting the desired state definition right in the first place. — location: [5075](kindle://book?action=open&asin=B09B5L4NVT&location=5075) ^ref-26726

---
While it’s possible to build your own toolchain to apply desired state management, typically you use a platform that already supports it. Kubernetes is one such tool that embraces this idea, and you can also achieve something similar using concepts such as autoscaling groups on a public cloud provider — location: [5079](kindle://book?action=open&asin=B09B5L4NVT&location=5079) ^ref-27029

---
As an operator, you are distanced from the low-level configuration—you can say something simple like “I want four instances spread across both data centers” and rely on your platform to ensure this is done for you. — location: [5088](kindle://book?action=open&asin=B09B5L4NVT&location=5088) ^ref-28272

---
having a fully automated deployment for microservice instances is a clear prerequisite for desired state management. — location: [5102](kindle://book?action=open&asin=B09B5L4NVT&location=5102) ^ref-35630

---
The shift with GitOps is that this tooling is making use of capabilities inside Kubernetes to help manage applications rather than just infrastructure. — location: [5120](kindle://book?action=open&asin=B09B5L4NVT&location=5120) ^ref-33824

---
When it comes to the approaches and tooling we can use for our microservice workloads, we have loads of options. But we should look at these options in terms of the principles I just outlined. — location: [5130](kindle://book?action=open&asin=B09B5L4NVT&location=5130) ^ref-18115

---
We want our microservices to run in an isolated fashion and to ideally be deployed in a way that avoids downtime. We want the tooling we pick to allow us to embrace a culture of automation, define our infrastructure and application configuration in code, and ideally also manage desired state for us. — location: [5132](kindle://book?action=open&asin=B09B5L4NVT&location=5132) ^ref-59524

---
The problem is that if you are working only at the level of a single physical machine, implementing concepts like desired state management, zero-downtime deployment, and so on requires us to work at a higher level of abstraction, using some sort of management layer on top. These types of systems are more commonly used in conjunction with virtual machines, — location: [5160](kindle://book?action=open&asin=B09B5L4NVT&location=5160) ^ref-18786

---
The more hosts the hypervisor manages, the more resources it needs. At a certain point, this overhead becomes a constraint in slicing up your physical infrastructure any further. — location: [5201](kindle://book?action=open&asin=B09B5L4NVT&location=5201) ^ref-52376

---
The issue is that many people are making use of managed VMs provided by traditional virtualization platforms like the ones provided by VMware, which, while they may theoretically allow for automation, are typically not used in this context. Instead these platforms tend to be under the central control of a dedicated operations team, and the ability to directly automate against them can be restricted as a result. — location: [5210](kindle://book?action=open&asin=B09B5L4NVT&location=5210) ^ref-50916

---
If you need the stricter isolation levels that they can bring, or you don’t have the ability to containerize your application, VMs can be a great choice. — location: [5216](kindle://book?action=open&asin=B09B5L4NVT&location=5216) ^ref-9412

---
The container concept, popularized by Docker, and allied with a supporting container orchestration platform like Kubernetes, has become many people’s go-to choice for running microservice architectures at scale. — location: [5222](kindle://book?action=open&asin=B09B5L4NVT&location=5222) ^ref-5947

---
Although Windows containers are very much a thing, it has been Linux operating systems that containers have had the biggest impact on so far. — location: [5229](kindle://book?action=open&asin=B09B5L4NVT&location=5229) ^ref-24649

---
The Linux kernel’s job is maintaining this tree of processes, ensuring that only permitted users can access the processes. — location: [5232](kindle://book?action=open&asin=B09B5L4NVT&location=5232) ^ref-53117

---
Additionally, the Linux kernel is capable of assigning resources to these different processes—this is all part and parcel of building a viable multiuser operating system, where you don’t want the activities of one user to kill the rest of the system. — location: [5232](kindle://book?action=open&asin=B09B5L4NVT&location=5232) ^ref-5729

---
Containers running on the same machine make use of the same underlying kernel (although there are exceptions to this rule that we’ll explore shortly). — location: [5234](kindle://book?action=open&asin=B09B5L4NVT&location=5234) ^ref-3462

---
Rather than managing processes directly, you can think of a container as an abstraction over a subtree of the overall system process tree, with the kernel doing all the hard work. These containers can have physical resources allocated to them, something the kernel handles for us. — location: [5235](kindle://book?action=open&asin=B09B5L4NVT&location=5235) ^ref-48010

---
This means that our host operating system could run Ubuntu, and our containers CentOS, as long as they could both run as part of the same underlying kernel. — location: [5245](kindle://book?action=open&asin=B09B5L4NVT&location=5245) ^ref-14764

---
With containers, we don’t just benefit from the resources saved by not needing a hypervisor; we also gain in terms of feedback. Linux containers are much faster to provision than full-fat virtual machines. — location: [5249](kindle://book?action=open&asin=B09B5L4NVT&location=5249) ^ref-25517

---
Due to the more lightweight nature of containers, we can have many more of them running on the same hardware than would be possible with VMs. — location: [5253](kindle://book?action=open&asin=B09B5L4NVT&location=5253) ^ref-63932

---
I’ve seen more than one project provision a large AWS EC2 instance and run multiple containers on it to get the best of both worlds: an on-demand ephemeral compute platform in the form of EC2, coupled with highly flexible and fast containers running on top of it. — location: [5261](kindle://book?action=open&asin=B09B5L4NVT&location=5261) ^ref-33692

---
the container orchestration systems and underlying container runtimes have done a good job of examining how to better run container workloads so this isolation is improved, but you will need to give due thought to the sorts of workloads you want to run. — location: [5273](kindle://book?action=open&asin=B09B5L4NVT&location=5273) ^ref-61666

---
It was with the delivery of Windows Server 2016 that a lot of this changed, and since then Windows containers have continued to evolve. — location: [5284](kindle://book?action=open&asin=B09B5L4NVT&location=5284) ^ref-63234

---
Remember that you need to run an operating system inside each container, so when downloading a container image, you’re also downloading an operating system. — location: [5286](kindle://book?action=open&asin=B09B5L4NVT&location=5286) ^ref-17377

---
Windows, though, is big—so big that it made containers very heavy, not just in terms of the size of the images but also in terms of the resources required to run them. — location: [5287](kindle://book?action=open&asin=B09B5L4NVT&location=5287) ^ref-41578

---
Microsoft reacted to this by creating a cut-down operating system called Windows Nano Server. The idea is that Nano Server should have a small-footprint OS and be capable of running things like microservice instances. — location: [5288](kindle://book?action=open&asin=B09B5L4NVT&location=5288) ^ref-9938

---
Nano Server would still be well over 1 GB in size, compared to small-footprint Linux operating systems like Alpine that would take up only a few megabytes. — location: [5291](kindle://book?action=open&asin=B09B5L4NVT&location=5291) ^ref-2880

---
Of special interest in the world of Windows containers is the fact that they support different levels of isolation. — location: [5294](kindle://book?action=open&asin=B09B5L4NVT&location=5294) ^ref-45119

---
Firecracker, which is confusingly called a kernel-based VM. Firecracker has proved popular as an implementation detail of service offerings like AWS Lambda, where there is a need to fully isolate workloads from different customers while still trying to keep spin-up time down and reduce the operational footprint of the workloads. — location: [5309](kindle://book?action=open&asin=B09B5L4NVT&location=5309) ^ref-5138

---
Containers were in limited use before the emergence of Docker pushed the concept mainstream. — location: [5313](kindle://book?action=open&asin=B09B5L4NVT&location=5313) ^ref-8312

---
The Docker toolchain handles much of the work around containers. Docker manages the container provisioning, handles some of the networking problems for you, and even provides its own registry concept that allows you to store Docker applications. — location: [5315](kindle://book?action=open&asin=B09B5L4NVT&location=5315) ^ref-32811

---
Before Docker, we didn’t have the concept of an “image” for containers—this aspect, along with a much nicer set of tools for working with containers, helped containers become much easier to use. — location: [5316](kindle://book?action=open&asin=B09B5L4NVT&location=5316) ^ref-54453

---
The Docker image abstraction is a useful one for us, as the details of how our microservice is implemented are hidden. — location: [5318](kindle://book?action=open&asin=B09B5L4NVT&location=5318) ^ref-15664

---
We have the builds for our microservice create a Docker image as a build artifact and store the image in the Docker registry, and away we go. — location: [5319](kindle://book?action=open&asin=B09B5L4NVT&location=5319) ^ref-47327

---
Previously, I might have used a tool like Vagrant that allows me to host multiple independent VMs on my development machine. This would allow me to have a production-like VM running my service instances locally. This was a pretty heavyweight approach, though, and I’d be limited in how many VMs I could run. — location: [5322](kindle://book?action=open&asin=B09B5L4NVT&location=5322) ^ref-60086

---
With Docker, it’s easy just to run Docker directly on my developer machine, probably using Docker Desktop. — location: [5324](kindle://book?action=open&asin=B09B5L4NVT&location=5324) ^ref-31239

---
Now I can just build a Docker image for my microservice instance, or pull down a prebuilt image, and run it locally. — location: [5325](kindle://book?action=open&asin=B09B5L4NVT&location=5325) ^ref-5875

---
These Docker images can (and should) be identical to the container image that I will eventually run in production. — location: [5326](kindle://book?action=open&asin=B09B5L4NVT&location=5326) ^ref-34767

---
When Docker first emerged, its scope was limited to managing containers on one machine. — location: [5327](kindle://book?action=open&asin=B09B5L4NVT&location=5327) ^ref-2865

---
Really, though, when it comes to managing lots of containers across many machines, Kubernetes is king here, even if you might use the Docker toolchain for building and managing individual containers. — location: [5331](kindle://book?action=open&asin=B09B5L4NVT&location=5331) ^ref-2979

---
Docker made containers significantly more viable as a concept. We get our isolation but at a manageable cost. We also hide underlying technology, allowing us to mix different tech stacks. — location: [5335](kindle://book?action=open&asin=B09B5L4NVT&location=5335) ^ref-13330

---
When it comes to implementing concepts like desired state management, though, we’ll need something like Kubernetes to handle it for us. — location: [5336](kindle://book?action=open&asin=B09B5L4NVT&location=5336) ^ref-33485

---
That said, I still feel that these application containers have enough downsides that you should challenge yourself to see whether they are really required. First among the downsides is that they inevitably constrain technology choice. You have to buy into a technology stack. This can limit not only the technology choices for the implementation of the service itself but also the options you have in terms of automation and management of your systems. — location: [5352](kindle://book?action=open&asin=B09B5L4NVT&location=5352) ^ref-6407

---
Many of them tout the ability to manage clusters to support shared in-memory session state, something we absolutely want to avoid in any case due to the challenges this creates when scaling our services. — location: [5357](kindle://book?action=open&asin=B09B5L4NVT&location=5357) ^ref-58031

---
And remember, even if you do get value from technology-specific containers, they aren’t free. Aside from the fact that many of them are commercial and thus have a cost implication, they add a resource overhead in and of themselves. — location: [5363](kindle://book?action=open&asin=B09B5L4NVT&location=5363) ^ref-11720

---
Ultimately, this approach is again an attempt to optimize for scarcity of resources that simply may not hold up anymore. — location: [5365](kindle://book?action=open&asin=B09B5L4NVT&location=5365) ^ref-40699

---
