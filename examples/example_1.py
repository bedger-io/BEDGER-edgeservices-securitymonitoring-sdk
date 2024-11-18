import time
import bedger.edge.config as config
import bedger.edge.connection as connection
import bedger.edge.entities as entities


if __name__ == "__main__":
    events = [
        {"event_type": "EventA", "severity": entities.Severity.HIGH, "payload": {"key": "value1"}},
        {"event_type": "EventB", "severity": entities.Severity.LOW, "payload": {"key": "value2"}},
        {"event_type": "EventC", "severity": entities.Severity.CRITICAL, "payload": {"key": "value3"}},
    ]

    with connection.ConnectionManager(config.Config()) as conn:
        for event in events:
            time.sleep(1)
            conn.send_event(event["event_type"], event["severity"], event["payload"])
