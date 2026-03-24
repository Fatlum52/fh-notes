+++
title = "Week 05"
date = 2026-03-24
[taxonomies]
authors = ["fatlum"]
tags = ["Vesys"]
+++

---

# Websocket

## Bank Uebung mit websockets

- WS-Server hat einen local-bank
- Client baut verbindung zu WS-Server
- client baut verbindung auf
- wenn ok kommt von server, schreibt man das onMessage() mit q.put in die Queue
- onMessage() läuft in eigenen Thread
- Statt BlockingQueue kann man auch SynchronousQueue oder Exchanger nehmen
- man kann trennen ob es updates oder commandos sind, indem man eines als TXT überträgt und das andere Binär
- wenn man zwei deposit gleichzeitig macht, kein problem, weil gui ist single threaded
- Platform run later, wird im FX thread gemacht, nachdem die offiziellen Ops gemacht werden
- Zu lösen:
  - kommunizieren über Queue
  - Bei änderungen alle notifizieren

```java
deposit {
    ws.send()
    q.take()
}

```java
WSServer {
    Bank bank;

    main {
        ...
    }

    @onMessage
    public onMessage() {
        ...
    }
}


public class RequestEncoder implements Encoder.BinaryStream<Command> {
 
    @Override
    public void encode(Command cmd, OutputStream os) throws EncodeException, IOException {
        ObjectOutputStream oos = new ObjectOutputStream(os);
        oos.writeObject(cmd);
    }
 
}

public class RequestDecoder implements Decoder.BinaryStream<Command> {
 
    @Override
    public Command decode(InputStream is) throws DecodeException {
        try {
            return (Command) new ObjectInputStream(is).readObject();
        } catch (Exception e) {
            throw new RuntimeException();
        }
    }
 
}

public class WSDriver implements Bankdriver.Driver

BlockingQuee
```
