<?php

# From Laravel-Excel https://github.com/SpartnerNL/Laravel-Excel

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