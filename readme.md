MetaTorrent
===========

MetaTorrent is a user friendly application that allows users to maintain an easy to search self hosted database of all available torrents and to easily publish new torrents to the Internet.

#Purpose

A re-occuring motive in websites built around bittorrent is robustness.
While such websites have accomplished this beyond expectation, it seems prudent to design a user-friendly way to escalate the perpetual game of wackamole to new and interesting levels.

#Method of robustness

This software is an exercise to see how simple a solution to the problem I can present.
Every hour (user modifable) the node will poll a list of peers for new torrents added to the network.
Each instance of the software will present a http interface to re-pubish torrents it has acquired or published.

#Effcient polling

For each peer, a node will record a timestamp of newest record polled from each peer.
A new poll to a peer includes this timestamp and will return up to 1000 (modifiable) records in chronological order after that timestamp. This way a single poll will not be a drain on bandwidth and processing, and over time all new torrents are propgated.

Ideal use case is that each node will maintain 20 peers, polling each once an hour.

#User Interface and Torrent Search

Each torrent can include an up to 80 character title, and a 200 character description.
A hashtag based system is advised to permit ease of searching the local database.

The user interface is intended to be as simple as possible.
Ideally, the user simply uses the torrent client they already use to generate a magnet link or BTIH. Then the torrent will be added to and propogated via the network.
