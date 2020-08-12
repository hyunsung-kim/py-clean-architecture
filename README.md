<p align="center">
    <img src="clean_arch.png">
</p>
# Clean Architecture


## 용어 및 기술
- [Inject](https://github.com/ivankorobkov/python-inject)
- [dependency-injector](https://github.com/ets-labs/python-dependency-injector)
- [Term](https://pusher.com/tutorials/clean-architecture-introduction)


## Terminology
- Adapter: The adapters, also called interface adapters, are the translators between the domain and the infrastructure.
- Port: In application Layer, Port is an interface of Adapter.
- Boundary: In application Layer, Boundary is an interface of Presenter.
- Use Case: The use cases are the business rules for a specific application. 
- Infrastructure: This layer is where all the I/O components go: the UI, database, frameworks, devices, etc.
- Entity: An entity is a set of related business rules that are critical to the function of the application.


## Reference
- [The Clean Architecture in Python. How to write testable and flexible code](https://breadcrumbscollector.tech/the-clean-architecture-in-python-how-to-write-testable-and-flexible-code/)
- [Python으로 클린 아키텍처 적용하기](https://velog.io/@jahoy/Python%EC%9C%BC%EB%A1%9C-Clean-Architecture-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)
- [[Python] Django, Clean Architecture 연구하기](https://medium.com/@erish/python-django-clean-architecture-%EC%97%B0%EA%B5%AC%ED%95%98%EA%B8%B0-591d7a555059)
- [Clean architectures in Python: a step-by-step example](https://www.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/)
