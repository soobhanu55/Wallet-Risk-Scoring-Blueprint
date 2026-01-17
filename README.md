𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧: A technical blueprint for calculating risk scores for blockchain wallet addresses by querying live protocol data. It primarily focuses on the Compound V2 protocol to assess the financial health and potential risk factors of specific users.

𝐊𝐞𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:
- GraphQL Data Integration: Connects to The Graph subgraphs using gql to fetch granular account-level data directly from the blockchain.
- Protocol-Specific Analysis: Tracks token symbols, account health factors, and balance histories specifically for Compound V2 users.
- Bulk Processing: Designed to handle lists of wallet addresses and export calculated risk scores into standardized formats (CSV).
- Dynamic Querying: Features a robust transport layer with retry logic to ensure reliable data fetching from decentralized APIs.

𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐒𝐭𝐚𝐜𝐤:
- API/Querying: GraphQL (GQL library), Requests
- Data Processing: Pandas, NumPy
- Monitoring: TQDM (Progress tracking)
- Data Source: The Graph (Compound V2 Subgraph)
