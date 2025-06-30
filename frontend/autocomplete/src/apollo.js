// src/apollo.js
import { ApolloClient, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
    uri: "http://localhost:8000/graphql/", // backend local
    cache: new InMemoryCache(),
});

export default client;
