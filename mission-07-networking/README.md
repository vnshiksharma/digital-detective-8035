# Mission 7 — Computer Networks

## 1. Task / objective

Understand and explain eight core networking concepts, run a live connectivity test and DNS lookup, and explain what happens step by step when a website is opened in a browser.

## 2. Work completed

All three tasks completed: concept table, live terminal network commands with actual output, and a seven-step website-opening explanation.

## 3. Commands / tools used

```bash
ping -c 4 example.com
nslookup example.com
```

## 4. My understanding

### Task 7.1 — Eight Networking Concepts

| Concept | Explanation | Simple example |
|---------|-------------|----------------|
| **LAN** (Local Area Network) | A network connecting devices within a small area, such as a home, office, or school building, usually through Wi-Fi or an Ethernet cable | All devices connected to your home Wi-Fi router form a LAN |
| **MAN** (Metropolitan Area Network) | A network that spans a city or large campus, larger than a LAN but smaller than a WAN | A city-wide network linking all branches of a bank |
| **WAN** (Wide Area Network) | A network covering a very large geographic area — cities, countries, or the entire globe; the Internet is the largest WAN | A company connecting its offices in Mumbai and Delhi over leased lines |
| **DNS** (Domain Name System) | A global system that translates human-readable domain names (like `example.com`) into IP addresses (like `172.66.147.243`) that computers use to find each other | When you type `google.com`, DNS gives back the IP address your browser needs |
| **Router** | A device that forwards data packets between different networks, deciding the best path for each packet to reach its destination | Your home Wi-Fi router connects your LAN to your Internet Service Provider's WAN |
| **Protocol** | A set of agreed rules that define how data is formatted, transmitted, and received so that different devices can communicate reliably | HTTP defines how web pages are requested and delivered; TCP ensures packets arrive correctly |
| **Packet switching** | A method of sending data where the message is broken into small chunks called packets; each packet travels independently and is reassembled at the destination | Sending a large file over the Internet — it is split into hundreds of packets, some may take different routes, and all are joined back at the receiver |
| **Client-server** | A model where one computer (the client) requests a service and another computer (the server) provides it | Your browser (client) requests a web page from a web server; the server sends back the HTML |

---

### Task 7.2 — Live Connectivity and DNS Tests

**Connectivity test — `ping -c 4 example.com`:**

```
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=57 time=4.020 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=57 time=3.933 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=57 time=3.480 ms
64 bytes from 172.66.147.243: icmp_seq=3 ttl=57 time=3.574 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.480/3.752/4.020/0.229 ms
```

**DNS lookup — `nslookup example.com`:**

```
Server:   8.8.8.8
Address:  8.8.8.8#53

Non-authoritative answer:
Name:  example.com
Address: 104.20.23.154
Name:  example.com
Address: 172.66.147.243
```

> **Privacy note:** No private IP addresses or Wi-Fi names appear in the above output. The DNS server used (`8.8.8.8`) is Google's public DNS resolver.

**What connectivity testing checks:**

`ping` sends ICMP echo-request packets to a host and measures whether replies come back. If packets arrive with low latency and 0% packet loss (as here — 4/4 received, avg 3.75 ms), it confirms that the network path between this machine and `example.com` is working correctly.

**What a DNS lookup displays:**

`nslookup` queries a DNS server and shows the IP address(es) mapped to the domain name. Here it returned two addresses (172.66.147.243 and 104.20.23.154), which are part of the CDN (content delivery network) that hosts `example.com`.

**Why DNS is required:**

Humans remember names like `example.com`, but routers forward packets using IP addresses like `172.66.147.243`. DNS acts as the phone book of the Internet, translating names into addresses automatically every time you visit a website.

---

### Task 7.3 — What Happens When You Open a Website (7 Steps)

1. **You type a URL in the browser.** For example, you type `https://example.com` and press Enter. The browser now needs to find the server that hosts this site.

2. **DNS lookup.** The browser asks a DNS resolver (such as 8.8.8.8) to translate `example.com` into an IP address. The resolver returns `172.66.147.243`. The browser now knows where to send its request.

3. **TCP connection established.** The browser uses the **TCP** protocol to open a reliable connection to the server at that IP address on port 443 (HTTPS). A three-way handshake (SYN → SYN-ACK → ACK) confirms both sides are ready to communicate.

4. **TLS/HTTPS handshake.** Because the URL starts with `https://`, the browser and server perform a TLS handshake to agree on encryption keys. All further communication is encrypted.

5. **Browser sends an HTTP GET request.** The browser sends a message to the server: "Please send me the content at `/`." This request travels as IP packets through your router and across the Internet.

6. **Server receives the request and sends a response.** The web server processes the request and sends back an HTTP response containing the HTML, CSS, and JavaScript of the page, broken into multiple packets that travel back through the network.

7. **Browser renders the page.** The browser reassembles the packets, parses the HTML, downloads any linked resources (images, scripts), and displays the finished web page on screen.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

All findings are documented in this README using actual output from the macOS Terminal.

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Explain networking concepts and website communication` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
