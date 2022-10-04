<?php

# From Laravel-Excel https://github.com/SpartnerNL/Laravel-Excel

# Observer Pattern

trait HasEventBus
{
    /**
     * @var array
     */
    protected $events = [];

    public function registerListeners(array $listeners)
    {
        foreach ($listeners as $event => $listener) {
            $this->events[$event][] = $listener;
        }
    }

    public function clearListeners()
    {
        $this->events = [];
    }

    public function raise($event)
    {
        foreach ($this->listeners($event) as $listener) {
            $listener($event);
        }
    }

    public function listeners($event): array
    {
        $name = \get_class($event);

        return $this->events[$name] ?? [];
    }
}

class NewsletterClient {
    public static function process($event)
    {
        $event->showMessage();
    }
} 

abstract class Event {}

class NewsletterSent extends Event {
    private $message;

    public function __construct($message)
    {
        $this->message = $message;   
    }

    public function showMessage() 
    {
        echo "Newsletter message: {$this->message}";
    }
}
class Newsletter {
    use HasEventBus;

    public function __construct()
    {
        $this->registerListeners([
            NewsletterSent::class => function (Event $event) {
                NewsletterClient::process($event);
            }
        ]);
    }

    public function prerareNewsletter()
    {
        echo "--> Preapre";
        echo "--> Add some custom data";
        echo "--> Send newsletter";
        $this->raise(new NewsletterSent("Hello there"));
    }
}