#!/usr/bin/env python
# -*- coding:utf-8 -*-

hm_conf = {
    "debug_level": 2,
    "buffer_size": 8192,
    "endpoint_type": "hostname",
    "metric_prefix": "haproxy_",
    "falcon_client": "http://127.0.0.1:1988/v1/push",
    "metrics": ['qcur', 'scur', 'rate', 'status', 'ereq', 'drep', 'act', 'bck', 'qtime', 'ctime', 'rtime', 'ttime'],
    "stats_file": "/duitang/data/work/haproxy.sock",
}

# vim: set noet sw=4 ts=4 sts=4 ff=unix fenc=utf8:
