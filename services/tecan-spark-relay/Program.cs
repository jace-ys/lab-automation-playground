﻿using System;
using System.Threading;

using Serilog;
using Serilog.Formatting.Compact;
using ServiceStack.Redis;
using Tecan.At.Dragonfly.AutomationInterface;

namespace TecanSparkRelay
{
    class Program
    {
        static void Main(string[] args)
        {
            var cfg = new Config();
            var logger = new LoggerConfiguration().WriteTo.Console(new CompactJsonFormatter()).CreateLogger();

            var redis = new RedisClient(cfg.pubsub.Addr);
            var forwarder = new Forwarder.Forwarder(cfg.forwarder);

            var manager = new System.Manager(logger, forwarder, redis, cfg.pubsub.SubscriptionTopic, cfg.manager);
            var subscribe = new Thread(new ThreadStart(manager.Subscribe));

            subscribe.Start();
            logger.Information("manager.subscribe.started {channel}", cfg.pubsub.SubscriptionTopic);

            Console.CancelKeyPress += new ConsoleCancelEventHandler((sender, e) =>
            {
                logger.Information("service.teardown");
                manager.Unsubscribe();

                AutomationInterfaceFactory.Stop();
            });

            subscribe.Join();
            logger.Information("managed.subscribe.stopped");
        }
    }
}
