# Delete Queues In RabbitMQ

When using RabbitMQ (an excellent message broker for decoupling applications) you sometimes end up with queues you don’t want or need anymore. Deleting them is thankfully a straight-forward process but first-time users often don’t know how to do this.

Probably the easiest way to delete a queue is to use rabbitmqadmin which is supplied by RabbitMQ’s management plugin. Deleting a queue is as simple as running the following:

```
rabbitmqadmin delete queue name=queue_1
```

Obviously, replace ‘queue_1’ with the name of the queue you want to delete :)

If you want to delete all the queues then you will need a list of them which can be generated like so:

```
rabbitmqadmin -f bash list queues name
```

Then, simply run this one-liner:

```
for queue in `rabbitmqadmin -f bash list queues`; do echo $queue `rabbitmqadmin delete queue name=$queue`; done
```

[http://davidsj.co.uk/](http://davidsj.co.uk/blog/delete-queues-in-rabbitmq/)