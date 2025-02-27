<!-- START graphql-markdown -->

# WisdomAI API documentation (sample)

## Most up to date API docs

- [https://{your_account_url}.askwisdom.ai/graphql](https://{your_account_url}.askwisdom.ai/graphql)

## Queries used for loading the chat page

- GetCurrentUser https://www.graphdev.app/?id=local-9981a875-ba7f-453c-8e69-35dee8e763dd
- ListPlaybooks https://www.graphdev.app/?id=local-b2df6b75-28c6-4446-8fe6-1f03be4f8a00
- GetZSheetName https://www.graphdev.app/?id=local-5aeef25c-e4e1-484d-9751-af8baccfb687
- GetChatTools https://www.graphdev.app/?id=local-fa77dc50-11e7-4ed3-b996-8d4afa0cee96
- GetConversations https://www.graphdev.app/?id=local-683c7eb4-d135-4d56-9576-b11ccba6a4fb
- GetConversationNameAndDomain https://www.graphdev.app/?id=local-48f1bcee-87bd-44c0-83c0-55edfbe47dbb
- GetChatMessagesAndConversation https://www.graphdev.app/?id=local-c10276c7-faba-4e8b-8254-a816c24f3f56

## Contact & Support

For any queries or support, contact our API team at [**support@askwisdom.ai**](mailto\:support@askwisdom.ai).

## GraphQL Schema (Sample)

## Query

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="query.chatmessages">chatMessages</strong></td>
<td valign="top"><a href="#chatmessagesresponse">ChatMessagesResponse</a></td>
<td>

Returns all the messages for a chat session.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">conversationId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.chattools">chatTools</strong></td>
<td valign="top">[<a href="#chattool">ChatTool</a>!]!</td>
<td>Return the available chat tools</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">domainId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.conversation">conversation</strong></td>
<td valign="top"><a href="#chatconversation">ChatConversation</a></td>
<td>

Returns a specific conversation

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.conversations">conversations</strong></td>
<td valign="top"><a href="#chatconversationsresponse">ChatConversationsResponse</a></td>
<td>

Returns a list of conversations available to the current user (ordered by the most recent first)

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#conversationfilterinput">ConversationFilterInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.currentuser">currentUser</strong></td>
<td valign="top"><a href="#user">User</a>!</td>
<td>Get information about the current user</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.playbook">playbook</strong></td>
<td valign="top"><a href="#playbook">Playbook</a></td>
<td>Return a specific playbook</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">id</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.playbooks">playbooks</strong></td>
<td valign="top">[<a href="#playbook">Playbook</a>!]!</td>
<td>Return a list of playbooks</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">domainId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.zsheet">zSheet</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td>

Returns a zSheet by the id.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">id</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="query.zsheets">zSheets</strong></td>
<td valign="top"><a href="#zsheetsresult">ZSheetsResult</a></td>
<td>

Returns all the zSheets

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#zsheetsfilterinput">ZSheetsFilterInput</a></td>
<td></td>
</tr>
</tbody>
</table>

## Subscription

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="subscription.chat">chat</strong></td>
<td valign="top"><a href="#chatmessagediff">ChatMessageDiff</a></td>
<td>

Requests a new chat message

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">auth</td>
<td valign="top"><a href="#subscriptionauthinput">SubscriptionAuthInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">conversationId</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">createHiddenConversation</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">domainId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">idempotencyKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">manualModelSelection</td>
<td valign="top"><a href="#llmmodelcomponent">LLMModelComponent</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">query</td>
<td valign="top"><a href="#structuredquery">StructuredQuery</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">skipCompose</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">toolSelection</td>
<td valign="top"><a href="#toolselection">ToolSelection</a></td>
<td></td>
</tr>
</tbody>
</table>

## Objects

### AddFilter

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="addfilter.parsedfilter">parsedFilter</strong></td>
<td valign="top"><a href="#parsedfilterbody">ParsedFilterBody</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Ambiguity

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="ambiguity.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="ambiguity.egregiousness">egregiousness</strong></td>
<td valign="top"><a href="#ambiguityegregiousness">AmbiguityEgregiousness</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="ambiguity.egregiousness_reason">egregiousness_reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AssignRoleResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="assignroleresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Attributes

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="attributes.bold">bold</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.code">code</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.containerid">containerId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.derivedtablename">derivedTableName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.endline">endline</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.error">error</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.generatedcode">generatedCode</strong></td>
<td valign="top"><a href="#code">Code</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.generatingquery">generatingQuery</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.playbookid">playbookId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.progress">progress</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.sqldialect">sqlDialect</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.streamid">streamId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.subtext">subtext</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.thinking">thinking</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.tool">tool</strong></td>
<td valign="top"><a href="#chattoolname">ChatToolName</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="attributes.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### AuthConfigs

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="authconfigs.authtype">authType</strong></td>
<td valign="top"><a href="#authtype">AuthType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AutoCompleteColumnMetadata

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="autocompletecolumnmetadata.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="autocompletecolumnmetadata.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AutoCompleteMetadata

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="autocompletemetadata.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="autocompletemetadata.piecemetadata">pieceMetadata</strong></td>
<td valign="top"><a href="#autocompletecolumnmetadata">AutoCompleteColumnMetadata</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="autocompletemetadata.searchterms">searchTerms</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="autocompletemetadata.structuredpiece">structuredPiece</strong></td>
<td valign="top"><a href="#structuredquerypiece">StructuredQueryPiece</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AutoCompletePiece

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="autocompletepiece.metadata">metadata</strong></td>
<td valign="top"><a href="#autocompletemetadata">AutoCompleteMetadata</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="autocompletepiece.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AutoCompleteResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="autocompleteresponse.suggestions">suggestions</strong></td>
<td valign="top">[<a href="#autocompletesuggestion">AutoCompleteSuggestion</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### AutoCompleteSuggestion

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="autocompletesuggestion.pieces">pieces</strong></td>
<td valign="top">[<a href="#autocompletepiece">AutoCompletePiece</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### BigQueryConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfig.datasetfilters">datasetFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfig.projectid">projectId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfig.serviceaccountinfojsonbase64">serviceAccountInfoJsonBase64</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### BrowseObject

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="browseobject.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="browseobject.id">id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="browseobject.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### CacheRuntimeInfo

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="cacheruntimeinfo.codegenstrategy">codegenStrategy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cacheruntimeinfo.matchedresult">matchedResult</strong></td>
<td valign="top"><a href="#cachesearchresultruntimeinfo">CacheSearchResultRuntimeInfo</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cacheruntimeinfo.query">query</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cacheruntimeinfo.retrievals">retrievals</strong></td>
<td valign="top">[<a href="#cachesearchresultruntimeinfo">CacheSearchResultRuntimeInfo</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### CacheSearchResultRuntimeInfo

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="cachesearchresultruntimeinfo.matchscore">matchScore</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cachesearchresultruntimeinfo.matchedquery">matchedQuery</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cachesearchresultruntimeinfo.matchingsearchstrategy">matchingSearchStrategy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cachesearchresultruntimeinfo.originaltraceid">originalTraceId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cachesearchresultruntimeinfo.templatizedquery">templatizedQuery</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### Cell

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="cell.forecastrange">forecastRange</strong></td>
<td valign="top"><a href="#forecastrange">ForecastRange</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cell.hyperlink">hyperlink</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="cell.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatConversation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.ispinned">isPinned</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.latestmessagetimestamp">latestMessageTimestamp</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.summary">summary</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.type">type</strong></td>
<td valign="top"><a href="#conversationtype">ConversationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversation.user">user</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
</tbody>
</table>

### ChatConversationsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatconversationsresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#chatconversation">ChatConversation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatconversationsresponse.pageinfo">pageInfo</strong></td>
<td valign="top"><a href="#pageinfo">PageInfo</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessage

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.body">body</strong></td>
<td valign="top"><a href="#delta">Delta</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.datarefreshedat">dataRefreshedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.edited">edited</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.errorstrings">errorStrings</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.feedback">feedback</strong></td>
<td valign="top"><a href="#feedbacktype">FeedbackType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.intention">intention</strong></td>
<td valign="top"><a href="#queryintention">QueryIntention</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.interactionid">interactionId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.linkeddashboards">linkedDashboards</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.messageid">messageId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.sender">sender</strong></td>
<td valign="top"><a href="#chatmessagesender">ChatMessageSender</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.user">user</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.userid">userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessage.verifiedcodeusage">verifiedCodeUsage</strong></td>
<td valign="top"><a href="#verifiedcodeusagetype">VerifiedCodeUsageType</a></td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageAnnotation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.datasources">dataSources</strong></td>
<td valign="top">[<a href="#datasourceannotation">DataSourceAnnotation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.fields">fields</strong></td>
<td valign="top">[<a href="#fieldannotation">FieldAnnotation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.filters">filters</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.granularity">granularity</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.limit">limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageannotation.sorts">sorts</strong></td>
<td valign="top">[<a href="#sortannotation">SortAnnotation</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageDiff

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.bodydiff">bodyDiff</strong></td>
<td valign="top"><a href="#delta">Delta</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.datarefreshedat">dataRefreshedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.diffindex">diffIndex</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.errorstrings">errorStrings</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.inprogress">inProgress</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.intention">intention</strong></td>
<td valign="top"><a href="#queryintention">QueryIntention</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.messageid">messageId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.sender">sender</strong></td>
<td valign="top"><a href="#chatmessagesender">ChatMessageSender</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.userid">userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagediff.verifiedcodeusage">verifiedCodeUsage</strong></td>
<td valign="top"><a href="#verifiedcodeusagetype">VerifiedCodeUsageType</a></td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageExplanation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageexplanation.annotations">annotations</strong></td>
<td valign="top">[<a href="#chatmessageannotation">ChatMessageAnnotation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageexplanation.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageexplanation.relevantknowledge">relevantKnowledge</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessageexplanation.steps">steps</strong></td>
<td valign="top">[<a href="#metadatastep">MetadataStep</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageGeneratedCode

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagegeneratedcode.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagegeneratedcode.sqlcode">sqlCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagegeneratedcode.sqldialect">sqlDialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageGeneratedNLExplanation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagegeneratednlexplanation.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagegeneratednlexplanation.nlexplanation">nlExplanation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageMetadata

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.assumption">assumption</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.cacheitemid">cacheItemId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.cacheruntimeinfo">cacheRuntimeInfo</strong></td>
<td valign="top"><a href="#cacheruntimeinfo">CacheRuntimeInfo</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.datasource">dataSource</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.errorstrings">errorStrings</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.executedsql">executedSql</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.intention">intention</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.learnedknowledge">learnedKnowledge</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.messageid">messageId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.opentelemetrytraceid">opentelemetryTraceId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.query">query</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.ragprompt">ragPrompt</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.rcasql">rcaSql</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.semanticengineruntimeinfos">semanticEngineRuntimeInfos</strong></td>
<td valign="top">[<a href="#semanticengineruntimeinfo">SemanticEngineRuntimeInfo</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.sql">sql</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.sqldialect">sqlDialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagemetadata.sqlexecutionerrormessage">sqlExecutionErrorMessage</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageTrainingModeInfo

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagetrainingmodeinfo.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagetrainingmodeinfo.trainingmodelearnedknowledgelist">trainingModeLearnedKnowledgeList</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagetrainingmodeinfo.trainingmodelearnedmeasureslist">trainingModeLearnedMeasuresList</strong></td>
<td valign="top">[<a href="#measure">Measure</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessagesResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatmessagesresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#chatmessage">ChatMessage</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ChatQuestion

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chatquestion.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatquestion.question">question</strong></td>
<td valign="top"><a href="#chatmessage">ChatMessage</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatquestion.response">response</strong></td>
<td valign="top"><a href="#chatmessage">ChatMessage</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chatquestion.responsemetadata">responseMetadata</strong></td>
<td valign="top"><a href="#chatmessagemetadata">ChatMessageMetadata</a></td>
<td></td>
</tr>
</tbody>
</table>

### ChatTool

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="chattool.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chattool.name">name</strong></td>
<td valign="top"><a href="#chattoolname">ChatToolName</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="chattool.type">type</strong></td>
<td valign="top"><a href="#chattooltype">ChatToolType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Code

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="code.codestr">codeStr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="code.dialect">dialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### CodegenConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="codegenconfig.reducecodegenthinking">reduceCodegenThinking</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### CollectVisualizationResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="collectvisualizationresponse.data">data</strong></td>
<td valign="top">[[<a href="#cell">Cell</a>!]!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="collectvisualizationresponse.hasmore">hasMore</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ColumnIdentifier

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="columnidentifier.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ColumnLocation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="columnlocation.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnlocation.zsheetname">zSheetName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ColumnMetadata

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="columnmetadata.columndatatype">columnDataType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnmetadata.columndescription">columnDescription</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnmetadata.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnmetadata.details">details</strong></td>
<td valign="top"><a href="#columndetails">ColumnDetails</a></td>
<td></td>
</tr>
</tbody>
</table>

### ColumnProperties

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.isdimensiongroupmember">isDimensionGroupMember</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.llmprompt">llmPrompt</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.sqlformula">sqlFormula</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnproperties.visibility">visibility</strong></td>
<td valign="top"><a href="#columnvisibility">ColumnVisibility</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Connection

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connection.details">details</strong></td>
<td valign="top"><a href="#connectiondetails">ConnectionDetails</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connection.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connection.status">status</strong></td>
<td valign="top"><a href="#connectionstatus">ConnectionStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionDatabasePairResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectiondatabasepairresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#connectionwithdatabases">ConnectionWithDatabases</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.bigquery">bigQuery</strong></td>
<td valign="top"><a href="#bigqueryconnectionconfig">BigQueryConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.connectiontype">connectionType</strong></td>
<td valign="top"><a href="#connectiontype">ConnectionType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.datasourcetype">dataSourceType</strong></td>
<td valign="top"><a href="#datasourcetype">DataSourceType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.databricks">databricks</strong></td>
<td valign="top"><a href="#databricksconnectionconfig">DatabricksConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.mysql">mysql</strong></td>
<td valign="top"><a href="#mysqlconnectionconfig">MySqlConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.postgres">postgres</strong></td>
<td valign="top"><a href="#postgresconnectionconfig">PostgresConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.redshift">redshift</strong></td>
<td valign="top"><a href="#redshiftconnectionconfig">RedshiftConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.snowflake">snowflake</strong></td>
<td valign="top"><a href="#snowflakeconnectionconfig">SnowflakeConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.sqlserver">sqlServer</strong></td>
<td valign="top"><a href="#sqlserverconnectionconfig">SqlServerConnectionConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetails.tableau">tableau</strong></td>
<td valign="top"><a href="#tableauconnectionconfig">TableauConnectionConfig</a></td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionStatus

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectionstatus.lastsuccessfulsynctimestamp">lastSuccessfulSyncTimestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectionstatus.lastsyncrun">lastSyncRun</strong></td>
<td valign="top"><a href="#connectionsyncrun">ConnectionSyncRun</a></td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionSyncRun

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectionsyncrun.endtimestamp">endTimestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectionsyncrun.starttimestamp">startTimestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectionsyncrun.status">status</strong></td>
<td valign="top"><a href="#connectionsyncstatus">ConnectionSyncStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionWithDatabases

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectionwithdatabases.connection">connection</strong></td>
<td valign="top"><a href="#connection">Connection</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectionwithdatabases.databases">databases</strong></td>
<td valign="top">[<a href="#browseobject">BrowseObject</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectionsresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#connection">Connection</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ConversationMessageCount

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="conversationmessagecount.count">count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="conversationmessagecount.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### CustomColors

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="customcolors.charts">charts</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### DBSchema

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dbschema.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dbschema.tables">tables</strong></td>
<td valign="top">[<a href="#dbtable">DBTable</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DBTable

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dbtable.columns">columns</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dbtable.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Dashboard

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.accesslevel">accessLevel</strong></td>
<td valign="top"><a href="#dashboardscope">DashboardScope</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.domains">domains</strong></td>
<td valign="top">[<a href="#zsheet">ZSheet</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.filters">filters</strong></td>
<td valign="top">[<a href="#dashboardfilterdefinition">DashboardFilterDefinition</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.owner">owner</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.sourcetype">sourceType</strong></td>
<td valign="top"><a href="#dashboardsourcetype">DashboardSourceType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.version">version</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboard.widgets">widgets</strong></td>
<td valign="top">[<a href="#dashboardwidget">DashboardWidget</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DashboardFilterDefinition

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardfilterdefinition.appliedstate">appliedState</strong></td>
<td valign="top">[<a href="#filterappliedstate">FilterAppliedState</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardfilterdefinition.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardfilterdefinition.parsedfilter">parsedFilter</strong></td>
<td valign="top"><a href="#parsedfilter">ParsedFilter</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DashboardSummaryDiff

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardsummarydiff.chunk">chunk</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DashboardWidget

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.datarefreshedat">dataRefreshedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.layout">layout</strong></td>
<td valign="top"><a href="#widgetlayout">WidgetLayout</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.markdowncontent">markdownContent</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.messageid">messageId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.nlquery">nlQuery</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.title">title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.usercanaskfollowup">userCanAskFollowUp</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.usercanvieworiginalmessage">userCanViewOriginalMessage</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.visualization">visualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.visualizationtype">visualizationType</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidget.widgettype">widgetType</strong></td>
<td valign="top"><a href="#widgettype">WidgetType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DashboardsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardsresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#dashboard">Dashboard</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DataSourceAnnotation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="datasourceannotation.connections">connections</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datasourceannotation.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datasourceannotation.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datasourceannotation.source">source</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datasourceannotation.type">type</strong></td>
<td valign="top"><a href="#dataframesourcetype">DataframeSourceType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Database

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="database.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="database.schemas">schemas</strong></td>
<td valign="top">[<a href="#dbschema">DBSchema</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DatabaseHierarchyForZSheetResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="databasehierarchyforzsheetresponse.databases">databases</strong></td>
<td valign="top">[<a href="#database">Database</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databasehierarchyforzsheetresponse.dialect">dialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DatabaseHierarchyResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="databasehierarchyresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#schema">Schema</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DatabricksConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfig.catalogfilters">catalogFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfig.clientid">clientId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfig.clientsecret">clientSecret</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfig.hostname">hostname</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfig.httppath">httpPath</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeColumn

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.alias">alias</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.annotation">annotation</strong></td>
<td valign="top"><a href="#fieldannotation">FieldAnnotation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.base">base</strong></td>
<td valign="top"><a href="#expressionbase">ExpressionBase</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.dateunit">dateUnit</strong></td>
<td valign="top"><a href="#dateunit">DateUnit</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.location">location</strong></td>
<td valign="top"><a href="#zsheetcolumnlocation">ZSheetColumnLocation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.properties">properties</strong></td>
<td valign="top"><a href="#columnproperties">ColumnProperties</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.tablename">tableName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.uniqueref">uniqueRef</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumn.zsheet">zsheet</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeExpression

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframeexpression.flattened">flattened</strong></td>
<td valign="top">[<a href="#dataframesingleexpressiononeof">DataframeSingleExpressionOneOf</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeFunction

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframefunction.argumentsindexes">argumentsIndexes</strong></td>
<td valign="top">[<a href="#int">Int</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframefunction.type">type</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeLiteral

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframeliteral.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeRawExpression

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframerawexpression.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeSingleExpressionOneOf

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeof.column">column</strong></td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeof.function">function</strong></td>
<td valign="top"><a href="#dataframefunction">DataframeFunction</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeof.literal">literal</strong></td>
<td valign="top"><a href="#dataframeliteral">DataframeLiteral</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeof.raw">raw</strong></td>
<td valign="top"><a href="#dataframerawexpression">DataframeRawExpression</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeof.subquery">subquery</strong></td>
<td valign="top"><a href="#dataframesubquery">DataframeSubquery</a></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeSubquery

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframesubquery.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesubquery.rawcodecache">rawCodeCache</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### DateTimeDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="datetimedetails.end">end</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datetimedetails.histogram">histogram</strong></td>
<td valign="top"><a href="#histogram">Histogram</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="datetimedetails.start">start</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DeleteUsersResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deleteusersresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DeliveryConfigEmail

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deliveryconfigemail.to">to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DeliveryConfigSlack

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deliveryconfigslack.channel">channel</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Delta

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="delta.ops">ops</strong></td>
<td valign="top">[<a href="#operation">Operation</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DeltaElement

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.column">column</strong> ⚠️</td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a></td>
<td>
<p>⚠️ <strong>DEPRECATED</strong></p>
<blockquote>

Use expression instead

</blockquote>
</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.reference">reference</strong></td>
<td valign="top"><a href="#reference">Reference</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.referredmessageid">referredMessageId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.refinementaction">refinementAction</strong></td>
<td valign="top"><a href="#refinementactiontype">RefinementActionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.text">text</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.textartifact">textArtifact</strong></td>
<td valign="top"><a href="#textartifact">TextArtifact</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.visualization">visualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="deltaelement.vizreference">vizReference</strong></td>
<td valign="top"><a href="#vizreference">VizReference</a></td>
<td></td>
</tr>
</tbody>
</table>

### DomainCrawlRun

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlrun.endtime">endTime</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlrun.starttime">startTime</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlrun.status">status</strong></td>
<td valign="top"><a href="#jobstatus">JobStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DomainCrawlStatus

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlstatus.domainid">domainId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlstatus.lastcrawl">lastCrawl</strong></td>
<td valign="top"><a href="#domaincrawlrun">DomainCrawlRun</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="domaincrawlstatus.lastsuccessfulcrawltime">lastSuccessfulCrawlTime</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
</tbody>
</table>

### DomainsCrawlStatusResult

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="domainscrawlstatusresult.nodes">nodes</strong></td>
<td valign="top">[<a href="#domaincrawlstatus">DomainCrawlStatus</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DrillDown

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="drilldown.drillfrom">drillFrom</strong></td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="drilldown.drillto">drillTo</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### EditFilter

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="editfilter.filterid">filterId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="editfilter.parsedfilteredit">parsedFilterEdit</strong></td>
<td valign="top"><a href="#parsedfilteredit">ParsedFilterEdit</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### EvaluationRun

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.completedat">completedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.conversationids">conversationIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.evalsetid">evalSetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.evaluations">evaluations</strong></td>
<td valign="top">[[<a href="#promptevaluation">PromptEvaluation</a>!]!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.manualmodelselection">manualModelSelection</strong></td>
<td valign="top"><a href="#llmmodelcomponent">LLMModelComponent</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.promptpairs">promptPairs</strong></td>
<td valign="top">[[<a href="#promptsqlpair">PromptSQLPair</a>!]!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="evaluationrun.prompts">prompts</strong></td>
<td valign="top">[[<a href="#string">String</a>!]!]</td>
<td></td>
</tr>
</tbody>
</table>

### ExpressionBase

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="expressionbase.zsheetref">zsheetRef</strong></td>
<td valign="top"><a href="#zsheetref">ZSheetRef</a></td>
<td></td>
</tr>
</tbody>
</table>

### ExtractQuestionsFromTextResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="extractquestionsfromtextresponse.questions">questions</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### FieldAnnotation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.datasources">dataSources</strong></td>
<td valign="top">[<a href="#fielddatasource">FieldDataSource</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.datatype">dataType</strong></td>
<td valign="top"><a href="#fielddatatype">FieldDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.derivedfieldexpression">derivedFieldExpression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.explanation">explanation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.expression">expression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.location">location</strong></td>
<td valign="top"><a href="#columnlocation">ColumnLocation</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fieldannotation.sourcetype">sourceType</strong></td>
<td valign="top"><a href="#fieldsourcetype">FieldSourceType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### FieldDataSource

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="fielddatasource.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="fielddatasource.datasource">dataSource</strong></td>
<td valign="top"><a href="#datasourceannotation">DataSourceAnnotation</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Filter

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="filter.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filter.column">column</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filter.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### FilterAppliedState

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="filterappliedstate.filteridonwidget">filterIdOnWidget</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filterappliedstate.widgetid">widgetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### FilterMutation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="filtermutation.add">add</strong></td>
<td valign="top">[<a href="#addfilter">AddFilter</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filtermutation.edit">edit</strong></td>
<td valign="top">[<a href="#editfilter">EditFilter</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filtermutation.remove">remove</strong></td>
<td valign="top">[<a href="#removefilter">RemoveFilter</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### FilterOperation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="filteroperation.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filteroperation.id">id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ForecastRange

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="forecastrange.lowerbound">lowerBound</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="forecastrange.upperbound">upperBound</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### GenerateDerivedFieldResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.samplequestion">sampleQuestion</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.sampleresponsecode">sampleResponseCode</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.sampleresponsedialect">sampleResponseDialect</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.sqlexpression">sqlExpression</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.type">type</strong></td>
<td valign="top"><a href="#derivedfieldtype">DerivedFieldType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="generatederivedfieldresponse.visualization">visualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
</tbody>
</table>

### GetDomainPromptStringResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="getdomainpromptstringresponse.promptstring">promptString</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### GetDomainStatsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="getdomainstatsresponse.numcolumns">numColumns</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="getdomainstatsresponse.numrows">numRows</strong></td>
<td valign="top"><a href="#bigint">BigInt</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="getdomainstatsresponse.numtables">numTables</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### GetDomainWidgetsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="getdomainwidgetsresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="getdomainwidgetsresponse.widgets">widgets</strong></td>
<td valign="top">[<a href="#widget">Widget</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### GoogleSlidesResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="googleslidesresponse.slideurl">slideUrl</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Histogram

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="histogram.buckets">buckets</strong></td>
<td valign="top">[<a href="#histogramdata">HistogramData</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### HistogramData

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="histogramdata.count">count</strong></td>
<td valign="top"><a href="#bigint">BigInt</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="histogramdata.label">label</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="histogramdata.leftvalue">leftValue</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="histogramdata.rightvalue">rightValue</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### InviteUsersResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="inviteusersresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### InviteUsersToDomainResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="inviteuserstodomainresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### LHS

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="lhs.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="lhs.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestion

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestion.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestion.source">source</strong></td>
<td valign="top"><a href="#mmsuggestionsource">MMSuggestionSource</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestion.status">status</strong></td>
<td valign="top"><a href="#mmsuggestionstatus">MMSuggestionStatus</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestion.task">task</strong></td>
<td valign="top"><a href="#mmsuggestiontask">MMSuggestionTask</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestionresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#mmsuggestion">MMSuggestion</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTask

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.addcolumndescription">addColumnDescription</strong></td>
<td valign="top"><a href="#mmsuggestiontaskcolumndescription">MMSuggestionTaskColumnDescription</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.addlearnedformula">addLearnedFormula</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedformula">MMSuggestionTaskAddLearnedFormula</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.addlearnedknowledge">addLearnedKnowledge</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedknowledge">MMSuggestionTaskAddLearnedKnowledge</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.addlearnedmetric">addLearnedMetric</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedmetric">MMSuggestionTaskAddLearnedMetric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.addmissingjoin">addMissingJoin</strong></td>
<td valign="top"><a href="#mmsuggestiontaskjoin">MMSuggestionTaskJoin</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.clarifycolumnnames">clarifyColumnNames</strong></td>
<td valign="top"><a href="#mmsuggestiontaskcolumnnames">MMSuggestionTaskColumnNames</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.entertabledescription">enterTableDescription</strong></td>
<td valign="top"><a href="#mmgsuggestiontasktabledescription">MMgSuggestionTaskTableDescription</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.textsuggestion">textSuggestion</strong></td>
<td valign="top"><a href="#mmsuggestiontasktextsuggestion">MMSuggestionTaskTextSuggestion</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontask.type">type</strong></td>
<td valign="top"><a href="#mmsuggestiontasktype">MMSuggestionTaskType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedFormula

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.formuladescription">formulaDescription</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.formulaexpression">formulaExpression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.formulaname">formulaName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformula.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedKnowledge

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledge.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledge.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledge.knowledgestr">knowledgeStr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledge.messageid">messageId</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedMetric

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetric.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetric.metricdescription">metricDescription</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetric.metricexpression">metricExpression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetric.metricname">metricName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskColumnDescription

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescription.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescription.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescription.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescription.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskColumnNames

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnames.explanation">explanation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnames.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnames.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnames.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskJoin

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoin.leftcolumnname">leftColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoin.leftsourceid">leftSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoin.relationshiptype">relationshipType</strong></td>
<td valign="top"><a href="#zsheetrelationshiptype">ZSheetRelationshipType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoin.rightcolumnname">rightColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoin.rightsourceid">rightSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskTextSuggestion

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontasktextsuggestion.explanation">explanation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontasktextsuggestion.suggestion">suggestion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMgSuggestionTaskTableDescription

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmgsuggestiontasktabledescription.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmgsuggestiontasktabledescription.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmgsuggestiontasktabledescription.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Measure

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="measure.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measure.expression">expression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measure.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MeasureGroup

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="measuregroup.format">format</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measuregroup.label">label</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measuregroup.measures">measures</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### MetadataStep

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="metadatastep.scope">scope</strong></td>
<td valign="top"><a href="#metadatastepscope">MetadataStepScope</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="metadatastep.text">text</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MySqlConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfig.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfig.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfig.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### NullDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="nulldetails.histogram">histogram</strong></td>
<td valign="top"><a href="#histogram">Histogram</a></td>
<td></td>
</tr>
</tbody>
</table>

### NumericDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="numericdetails.histogram">histogram</strong></td>
<td valign="top"><a href="#histogram">Histogram</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="numericdetails.maximum">maximum</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="numericdetails.mean">mean</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="numericdetails.minimum">minimum</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### OnboardingState

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="onboardingstate.featuresonboarded">featuresOnboarded</strong></td>
<td valign="top">[<a href="#onboardingfeature">OnboardingFeature</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="onboardingstate.preference">preference</strong></td>
<td valign="top"><a href="#onboardingpreference">OnboardingPreference</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="onboardingstate.role">role</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="onboardingstate.roledepartment">roleDepartment</strong></td>
<td valign="top"><a href="#roledepartment">RoleDepartment</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="onboardingstate.trialstate">trialState</strong></td>
<td valign="top"><a href="#trialstate">TrialState</a></td>
<td></td>
</tr>
</tbody>
</table>

### OperateDataframeResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="operatedataframeresponse.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="operatedataframeresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Operation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="operation.attributes">attributes</strong></td>
<td valign="top"><a href="#attributes">Attributes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="operation.delete">delete</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="operation.insert">insert</strong></td>
<td valign="top"><a href="#deltaelement">DeltaElement</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="operation.retain">retain</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### OrFilterGroup

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="orfiltergroup.filters">filters</strong></td>
<td valign="top">[<a href="#parsedfilter">ParsedFilter</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### PageInfo

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="pageinfo.hasnextpage">hasNextPage</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="pageinfo.haspreviouspage">hasPreviousPage</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="pageinfo.limit">limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="pageinfo.offset">offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PaginateOperation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="paginateoperation.limit">limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="paginateoperation.offset">offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Pagination

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="pagination.pageindex">pageIndex</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="pagination.pagesize">pageSize</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ParsedFilter

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilter.filterid">filterId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilter.lhs">lhs</strong></td>
<td valign="top"><a href="#lhs">LHS</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilter.operator">operator</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilter.orfiltergroup">orFilterGroup</strong></td>
<td valign="top"><a href="#orfiltergroup">OrFilterGroup</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilter.rhs">rhs</strong></td>
<td valign="top"><a href="#rhs">RHS</a></td>
<td></td>
</tr>
</tbody>
</table>

### ParsedFilterBody

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterbody.lhs">lhs</strong></td>
<td valign="top"><a href="#lhs">LHS</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterbody.operator">operator</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterbody.rhs">rhs</strong></td>
<td valign="top"><a href="#rhs">RHS</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ParsedFilterEdit

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilteredit.operator">operator</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilteredit.orgroupmutation">orGroupMutation</strong></td>
<td valign="top"><a href="#filtermutation">FilterMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilteredit.rhs">rhs</strong></td>
<td valign="top"><a href="#rhs">RHS</a></td>
<td></td>
</tr>
</tbody>
</table>

### Playbook

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="playbook.createdat">createdAt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.deletedat">deletedAt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.domainid">domainId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.markdown">markdown</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.ownerid">ownerId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.title">title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbook.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### PossibleColumnLiteralsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnliteralsresponse.literals">literals</strong></td>
<td valign="top">[<a href="#dataframeliteral">DataframeLiteral</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### PossibleColumnsForVizEditorResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnsforvizeditorresponse.columns">columns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnsforvizeditorresponse.dataframecolumns">dataframeColumns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnsforvizeditorresponse.metrics">metrics</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnsforvizeditorresponse.popularcolumns">popularColumns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### PossibleColumnsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="possiblecolumnsresponse.columns">columns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### PostgresConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfig.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfig.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfig.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processcsvresponse.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvresponse.tableid">tableId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PromptEvaluation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.generatederror">generatedError</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.generatedvisualization">generatedVisualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.gterror">gtError</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.gtvisualization">gtVisualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.manualfeedback">manualFeedback</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.manualscore">manualScore</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.softevalfeedback">softEvalFeedback</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptevaluation.softevalscore">softEvalScore</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### PromptSQLPair

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="promptsqlpair.prompt">prompt</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptsqlpair.sql">sql</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ProxyConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfig.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfig.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PublicSlackConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="publicslackconnectionconfig.appid">appId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="publicslackconnectionconfig.appname">appName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="publicslackconnectionconfig.teamid">teamId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="publicslackconnectionconfig.teamname">teamName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PublicTenantConfigs

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="publictenantconfigs.customcolors">customColors</strong></td>
<td valign="top"><a href="#customcolors">CustomColors</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="publictenantconfigs.fystartmonth">fyStartMonth</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="publictenantconfigs.slackconnection">slackConnection</strong></td>
<td valign="top"><a href="#publicslackconnectionconfig">PublicSlackConnectionConfig</a></td>
<td></td>
</tr>
</tbody>
</table>

### QueryIntention

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="queryintention.dependencies">dependencies</strong></td>
<td valign="top">[<a href="#int">Int</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="queryintention.instruction">instruction</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="queryintention.reasoning">reasoning</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="queryintention.summary">summary</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="queryintention.type">type</strong></td>
<td valign="top"><a href="#queryintentiontype">QueryIntentionType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItem

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.code">code</strong></td>
<td valign="top"><a href="#code">Code</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.domain">domain</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.invalidatedat">invalidatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.invalidatedby">invalidatedBy</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.isvalidated">isValidated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.question">question</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.ratingsbad">ratingsBad</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.ratingsgood">ratingsGood</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.sourcedetails">sourceDetails</strong></td>
<td valign="top"><a href="#questionbankitemsourcedetails">QuestionBankItemSourceDetails</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.timesasked">timesAsked</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.validatedat">validatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitem.validatedby">validatedBy</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItemSourceDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsourcedetails.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsourcedetails.messageid">messageId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItemsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#questionbankitem">QuestionBankItem</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsresponse.pageinfo">pageInfo</strong></td>
<td valign="top"><a href="#pageinfo">PageInfo</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### QuestionsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionsresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#chatquestion">ChatQuestion</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionsresponse.pageinfo">pageInfo</strong></td>
<td valign="top"><a href="#pageinfo">PageInfo</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RHS

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhs.literal">literal</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhs.range">range</strong></td>
<td valign="top"><a href="#rhsrange">RHSRange</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhs.set">set</strong></td>
<td valign="top"><a href="#rhsset">RHSSet</a></td>
<td></td>
</tr>
</tbody>
</table>

### RHSRange

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhsrange.closed">closed</strong></td>
<td valign="top"><a href="#intervalclosed">IntervalClosed</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsrange.end">end</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsrange.start">start</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RHSSet

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhsset.values">values</strong></td>
<td valign="top">[<a href="#dataframeexpression">DataframeExpression</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### RecentlyUsedDomain

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="recentlyuseddomain.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="recentlyuseddomain.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="recentlyuseddomain.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RecommendedQuestionsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="recommendedquestionsresponse.questions">questions</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### RedshiftConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfig.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfig.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfig.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Reference

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="reference.chunktext">chunkText</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.id">id</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.index">index</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.link">link</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.page">page</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.primarykey">primaryKey</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.rowdata">rowData</strong></td>
<td valign="top"><a href="#json">JSON</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.title">title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="reference.zsheetid">zsheetId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### RemoveColumn

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="removecolumn.column">column</strong></td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RemoveFilter

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="removefilter.filterid">filterId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ResponseStatus

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="responsestatus.code">code</strong></td>
<td valign="top"><a href="#statuscode">StatusCode</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="responsestatus.message">message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ReviewQuestionResult

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="reviewquestionresult.nodes">nodes</strong></td>
<td valign="top">[<a href="#questionbankitem">QuestionBankItem</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### Role

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="role.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="role.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RoleAssignment

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="roleassignment.role">role</strong></td>
<td valign="top"><a href="#role">Role</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="roleassignment.scopes">scopes</strong></td>
<td valign="top">[<a href="#scope">Scope</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="roleassignment.user">user</strong></td>
<td valign="top"><a href="#user">User</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Schedule

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="schedule.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="schedule.owner">owner</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="schedule.task">task</strong></td>
<td valign="top"><a href="#scheduletask">ScheduleTask</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="schedule.timing">timing</strong></td>
<td valign="top"><a href="#scheduletiming">ScheduleTiming</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleDelivery

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduledelivery.emailconfig">emailConfig</strong></td>
<td valign="top"><a href="#deliveryconfigemail">DeliveryConfigEmail</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduledelivery.slackconfig">slackConfig</strong></td>
<td valign="top"><a href="#deliveryconfigslack">DeliveryConfigSlack</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduledelivery.type">type</strong></td>
<td valign="top"><a href="#deliverytype">DeliveryType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleTask

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduletask.delivery">delivery</strong></td>
<td valign="top"><a href="#scheduledelivery">ScheduleDelivery</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletask.resourceid">resourceId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletask.resourcetitle">resourceTitle</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletask.type">type</strong></td>
<td valign="top"><a href="#scheduletasktype">ScheduleTaskType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleTiming

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduletiming.intervalinmins">intervalInMins</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletiming.starttime">startTime</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Schema

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="schema.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="schema.zsheets">zSheets</strong></td>
<td valign="top">[<a href="#zsheet">ZSheet</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### Scope

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scope.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scope.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scope.scopetype">scopeType</strong></td>
<td valign="top"><a href="#scopetype">ScopeType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SemanticEngineRuntimeInfo

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.callername">callerName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.columnfilter">columnFilter</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.query">query</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.semantichits">semanticHits</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.topkgretrievals">topKGRetrievals</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="semanticengineruntimeinfo.zsheetfilter">zsheetFilter</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SignedUrl

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="signedurl.buckettype">bucketType</strong></td>
<td valign="top"><a href="#buckettype">BucketType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="signedurl.key">key</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="signedurl.signedurl">signedUrl</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SnowflakeConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.account">account</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.privatekey">privateKey</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.proxyconfig">proxyConfig</strong></td>
<td valign="top"><a href="#proxyconfig">ProxyConfig</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.role">role</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.user">user</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfig.warehouse">warehouse</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SortAnnotation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sortannotation.columns">columns</strong></td>
<td valign="top">[<a href="#sortcolumnannotation">SortColumnAnnotation</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### SortColumn

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumn.column">column</strong></td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumn.order">order</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SortColumnAnnotation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumnannotation.column">column</strong></td>
<td valign="top"><a href="#columnidentifier">ColumnIdentifier</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumnannotation.nullsfirst">nullsFirst</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumnannotation.order">order</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SortOperation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sortoperation.columns">columns</strong></td>
<td valign="top">[<a href="#sortcolumn">SortColumn</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### SqlServerConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfig.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfig.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfig.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### StringDetails

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="stringdetails.distinctvalues">distinctValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="stringdetails.histogram">histogram</strong></td>
<td valign="top"><a href="#histogram">Histogram</a></td>
<td></td>
</tr>
</tbody>
</table>

### StructuredQueryPiece

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.action">action</strong></td>
<td valign="top"><a href="#refinementactiontype">RefinementActionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.column">column</strong></td>
<td valign="top"><a href="#dataframecolumn">DataframeColumn</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpression">DataframeExpression</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.playgroundqueryhint">playgroundQueryHint</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.text">text</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypiece.vizreference">vizReference</strong></td>
<td valign="top"><a href="#vizreference">VizReference</a></td>
<td></td>
</tr>
</tbody>
</table>

### Subtotal

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="subtotal.columns">columns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td>

Subtotals help in aggregating data at different levels. This currently only used for
drilled down data.

Example:

--- Starting table:

State, Population
CA, 1M
TX, 2M

Subtotals: []

--- Drill down by City:

State -> City, Population
CA, SF, 500K
CA, LA, 500K
TX, Austin, 1M
TX, Dallas, 1M

Subtotals: [
{
columns: [State],
data: [
[CA, 1M],
[TX, 2M]
]
}
]

--- Drill down by Gender:

State -> City -> Gender, Population
CA, SF, M, 250K
CA, SF, F, 250K
CA, LA, M, 250K
CA, LA, F, 250K
TX, Austin, M, 500K
TX, Austin, F, 500K
TX, Dallas, M, 500K
TX, Dallas, F, 500K

Subtotals: [
{
columns: [State],
data: [
[CA, 1M],
[TX, 2M]
]
},
{
columns: [State, City],
data: [
[CA, SF, 500K],
[CA, LA, 500K],
[TX, Austin, 1M],
[TX, Dallas, 1M]
]
}
]

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="subtotal.data">data</strong></td>
<td valign="top">[[<a href="#cell">Cell</a>!]!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="subtotal.visualizationid">visualizationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### TableauConnectionConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="tableauconnectionconfig.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="tableauconnectionconfig.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### TextArtifact

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="textartifact.artifactid">artifactId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="textartifact.content">content</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="textartifact.filterstrings">filterStrings</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="textartifact.hitcount">hitCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="textartifact.references">references</strong></td>
<td valign="top">[<a href="#reference">Reference</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### TrialState

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="trialstate.trialextensionreasons">trialExtensionReasons</strong></td>
<td valign="top">[<a href="#trialextensionreason">TrialExtensionReason</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="trialstate.triallengthindays">trialLengthInDays</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="trialstate.trialstartedon">trialStartedOn</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
</tbody>
</table>

### UnassignRoleResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="unassignroleresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UnstructuredIndexProperties

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexproperties.embedmetadatacolumns">embedMetadataColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexproperties.indexmetadatafacets">indexMetadataFacets</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexproperties.promptmetadatacolumns">promptMetadataColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexproperties.searchoutputcolumns">searchOutputColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexproperties.shouldembed">shouldEmbed</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateChatMessageResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessageresponse.chatmessage">chatMessage</strong></td>
<td valign="top"><a href="#chatmessage">ChatMessage</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessageresponse.traceid">traceId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateDerivedFieldResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updatederivedfieldresponse.sampleresponsecode">sampleResponseCode</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatederivedfieldresponse.sampleresponsedialect">sampleResponseDialect</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatederivedfieldresponse.visualization">visualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a></td>
<td></td>
</tr>
</tbody>
</table>

### UpdateRoleAssignmentsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updateroleassignmentsresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateScopeRoleAssignmentsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updatescoperoleassignmentsresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateVisualization

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updatevisualization.drilldown">drillDown</strong></td>
<td valign="top"><a href="#drilldown">DrillDown</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatevisualization.filtermutations">filterMutations</strong></td>
<td valign="top"><a href="#filtermutation">FilterMutation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatevisualization.removecolumn">removeColumn</strong></td>
<td valign="top"><a href="#removecolumn">RemoveColumn</a></td>
<td></td>
</tr>
</tbody>
</table>

### UpsertUserStateResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="upsertuserstateresponse.status">status</strong></td>
<td valign="top"><a href="#responsestatus">ResponseStatus</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### User

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="user.creationtimestamp">creationTimestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.email">email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.lastactivesessiontimestamp">lastActiveSessionTimestamp</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.profilepicture">profilePicture</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="user.roleassignments">roleAssignments</strong></td>
<td valign="top">[<a href="#roleassignment">RoleAssignment</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### Visualization

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="visualization.code">code</strong></td>
<td valign="top"><a href="#code">Code</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.columndisplayformats">columnDisplayFormats</strong></td>
<td valign="top">[<a href="#displayformat">DisplayFormat</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.columnorder">columnOrder</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.columns">columns</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.data">data</strong></td>
<td valign="top">[[<a href="#cell">Cell</a>!]!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.dimensions">dimensions</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.drilldownsequence">drillDownSequence</strong></td>
<td valign="top">[<a href="#dataframecolumn">DataframeColumn</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.filters">filters</strong></td>
<td valign="top">[<a href="#filteroperation">FilterOperation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.hasmore">hasMore</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.id">id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.measuregroups">measureGroups</strong></td>
<td valign="top">[<a href="#measuregroup">MeasureGroup</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.measures">measures</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.originaltype">originalType</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.pagination">pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.parsedfilters">parsedFilters</strong></td>
<td valign="top">[<a href="#parsedfilter">ParsedFilter</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.sortoperation">sortOperation</strong></td>
<td valign="top"><a href="#sortoperation">SortOperation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.subtotals">subtotals</strong></td>
<td valign="top">[<a href="#subtotal">Subtotal</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.title">title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.type">type</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.uniquedimensions">uniqueDimensions</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.unparsedfilters">unparsedFilters</strong></td>
<td valign="top">[<a href="#filteroperation">FilterOperation</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualization.updates">updates</strong></td>
<td valign="top">[<a href="#updatevisualization">UpdateVisualization</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### VizConfig

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="vizconfig.alwaysusecompactnumberformat">alwaysUseCompactNumberFormat</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizconfig.openshowdatapanelbydefault">openShowDataPanelByDefault</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### VizReference

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="vizreference.charttype">chartType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreference.dataframecollectedatms">dataframeCollectedAtMs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreference.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreference.hidden">hidden</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### Widget

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="widget.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widget.id">id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widget.query">query</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widget.title">title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widget.visualization">visualization</strong></td>
<td valign="top"><a href="#visualization">Visualization</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### WidgetLayout

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayout.height">height</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayout.left">left</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayout.top">top</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayout.width">width</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### WidgetMetadata

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="widgetmetadata.dialect">dialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetmetadata.sql">sql</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheet

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.codegenconfig">codegenConfig</strong></td>
<td valign="top"><a href="#codegenconfig">CodegenConfig</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.columns">columns</strong></td>
<td valign="top">[<a href="#zsheetcolumn">ZSheetColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#zsheetcolumnfilterinput">ZSheetColumnFilterInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">orderBy</td>
<td valign="top">[<a href="#zsheetcolumnorder">ZSheetColumnOrder</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.connection">connection</strong></td>
<td valign="top"><a href="#connection">Connection</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.domainsysteminstructions">domainSystemInstructions</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.entities">entities</strong></td>
<td valign="top">[<a href="#zsheetentity">ZSheetEntity</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.formulas">formulas</strong></td>
<td valign="top">[<a href="#zsheetderivedfield">ZSheetDerivedField</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#zsheetcolumnfilterinput">ZSheetColumnFilterInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.fystartmonth">fyStartMonth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.hiddensourceids">hiddenSourceIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.isusercsvdomain">isUserCSVDomain</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.isusercsvtable">isUserCSVTable</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.joins">joins</strong></td>
<td valign="top">[<a href="#zsheetjoin">ZSheetJoin</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.joinswith">joinsWith</strong></td>
<td valign="top">[<a href="#zsheetjoinwith">ZSheetJoinWith</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.knowledge">knowledge</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.location">location</strong></td>
<td valign="top"><a href="#zsheetlocation">ZSheetLocation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.measures">measures</strong></td>
<td valign="top">[<a href="#zsheetderivedfield">ZSheetDerivedField</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#zsheetcolumnfilterinput">ZSheetColumnFilterInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.sourcesql">sourceSql</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.sources">sources</strong></td>
<td valign="top">[<a href="#zsheet">ZSheet</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.type">type</strong></td>
<td valign="top"><a href="#zsheettype">ZSheetType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.version">version</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheet.vizconfig">vizConfig</strong></td>
<td valign="top"><a href="#vizconfig">VizConfig</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumn

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.aliases">aliases</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.contenttag">contentTag</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.defaultorder">defaultOrder</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.format">format</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.isforeignkey">isForeignKey</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.isprimarykey">isPrimaryKey</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.prioritized">prioritized</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.skipner">skipNer</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.unstructuredindexproperties">unstructuredIndexProperties</strong></td>
<td valign="top"><a href="#unstructuredindexproperties">UnstructuredIndexProperties</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.useridentificationinfo">userIdentificationInfo</strong></td>
<td valign="top"><a href="#useridentificationinfo">UserIdentificationInfo</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumn.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnLocation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocation.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocation.zsheetalias">zsheetAlias</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocation.zsheetref">zsheetRef</strong></td>
<td valign="top"><a href="#zsheetref">ZSheetRef</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnresponse.column">column</strong></td>
<td valign="top"><a href="#zsheetcolumn">ZSheetColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnresponse.zsheetversion">zsheetVersion</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDbObject

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.connectionid">connectionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.createdat">createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.databasename">databaseName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.hits">hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.isdeleted">isDeleted</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.islatest">isLatest</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.schemaname">schemaName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.sourcetype">sourceType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.updatedat">updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.version">version</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.zsheetjson">zSheetJson</strong></td>
<td valign="top"><a href="#json">JSON</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdbobject.zsheettype">zSheetType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDefaultOrderBy

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdefaultorderby.column">column</strong></td>
<td valign="top"><a href="#zsheetentitycolumn">ZSheetEntityColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdefaultorderby.order">order</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDeleteResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdeleteresponse.success">success</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdeleteresponse.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedField

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.aliases">aliases</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.contenttag">contentTag</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.datecolumnname">dateColumnName</strong></td>
<td valign="top"><a href="#zsheetcolumnlocation">ZSheetColumnLocation</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.defaultorder">defaultOrder</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.expression">expression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.format">format</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.formulatype">formulaType</strong></td>
<td valign="top"><a href="#formulatype">FormulaType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.groupbycolumns">groupByColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.isprimarykey">isPrimaryKey</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.llmprompt">llmPrompt</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.location">location</strong></td>
<td valign="top"><a href="#zsheetderivedfieldlocation">ZSheetDerivedFieldLocation</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.prioritized">prioritized</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.unstructuredindexproperties">unstructuredIndexProperties</strong></td>
<td valign="top"><a href="#unstructuredindexproperties">UnstructuredIndexProperties</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.useridentificationinfo">userIdentificationInfo</strong></td>
<td valign="top"><a href="#useridentificationinfo">UserIdentificationInfo</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfield.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedFieldLocation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldlocation.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldlocation.zsheetname">zSheetName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedFieldSaveResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldsaveresponse.formula">formula</strong></td>
<td valign="top"><a href="#zsheetderivedfield">ZSheetDerivedField</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldsaveresponse.measure">measure</strong></td>
<td valign="top"><a href="#zsheetderivedfield">ZSheetDerivedField</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntity

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.defaultcolumns">defaultColumns</strong></td>
<td valign="top">[<a href="#zsheetentitycolumn">ZSheetEntityColumn</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.defaultorderby">defaultOrderBy</strong></td>
<td valign="top"><a href="#zsheetdefaultorderby">ZSheetDefaultOrderBy</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.idcolumn">idColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumn">ZSheetEntityColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.namecolumn">nameColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumn">ZSheetEntityColumn</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentity.template">template</strong></td>
<td valign="top"><a href="#zsheetentitytemplate">ZSheetEntityTemplate</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityCandidatesResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycandidatesresponse.nodes">nodes</strong></td>
<td valign="top">[<a href="#zsheetentity">ZSheetEntity</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityColumn

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumn.location">location</strong></td>
<td valign="top"><a href="#zsheetcolumnlocation">ZSheetColumnLocation</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumn.wildcardcolumn">wildcardColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumn">ZSheetEntityColumn</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumn.wildcardedurl">wildcardedUrl</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityDeleteResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitydeleteresponse.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitydeleteresponse.success">success</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitydeleteresponse.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityTemplate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.cardtemplate">cardTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.cardtemplateoptionalcolumns">cardTemplateOptionalColumns</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.cardtemplaterequiredcolumns">cardTemplateRequiredColumns</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.listtemplate">listTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.listtemplateoptionalcolumns">listTemplateOptionalColumns</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.listtemplaterequiredcolumns">listTemplateRequiredColumns</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitytemplate.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetJoin

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoin.leftcolumnname">leftColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoin.leftsource">leftSource</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoin.relationshiptype">relationshipType</strong></td>
<td valign="top"><a href="#zsheetrelationshiptype">ZSheetRelationshipType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoin.rightcolumnname">rightColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoin.rightsource">rightSource</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetJoinWith

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoinwith.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoinwith.othercolumnname">otherColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoinwith.othersource">otherSource</strong></td>
<td valign="top"><a href="#zsheet">ZSheet</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoinwith.relationshiptype">relationshipType</strong></td>
<td valign="top"><a href="#zsheetrelationshiptype">ZSheetRelationshipType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetLocation

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocation.connectionid">connectionId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocation.database">database</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocation.schema">schema</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocation.tabletype">tableType</strong></td>
<td valign="top"><a href="#zsheettabletype">ZSheetTableType</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetRef

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetref.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetref.uuid">uuid</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetSampleDataResult

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetsampledataresult.data">data</strong></td>
<td valign="top">[[<a href="#string">String</a>!]!]!</td>
<td>

Sample data where the first row represents the columns

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetsampledataresult.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetsResult

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetsresult.nodes">nodes</strong></td>
<td valign="top">[<a href="#zsheet">ZSheet</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

## Inputs

### AddColumnMutationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="addcolumnmutationinput.column">column</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AddParsedFilterMutation

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="addparsedfiltermutation.parsedfilter">parsedFilter</strong></td>
<td valign="top"><a href="#parsedfilterinput">ParsedFilterInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### AllConversationFilterInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="allconversationfilterinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="allconversationfilterinput.latestmessageafter">latestMessageAfter</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="allconversationfilterinput.latestmessagebefore">latestMessageBefore</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="allconversationfilterinput.summarysearch">summarySearch</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="allconversationfilterinput.userid">userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### AssignRoleInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="assignroleinput.principalids">principalIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="assignroleinput.roleid">roleId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="assignroleinput.scopes">scopes</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### BaseDataframeColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="basedataframecolumninput.columnalias">columnAlias</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### BaseTableColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="basetablecolumninput.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="basetablecolumninput.tablealias">tableAlias</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="basetablecolumninput.tablezsheetid">tableZsheetId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### BigQueryConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfiginput.datasetfilters">datasetFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfiginput.projectid">projectId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="bigqueryconnectionconfiginput.serviceaccountinfojsonbase64">serviceAccountInfoJsonBase64</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### CodeInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="codeinput.codestr">codeStr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="codeinput.dialect">dialect</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### CodegenConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="codegenconfiginput.reducecodegenthinking">reduceCodegenThinking</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ColumnPropertiesInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.isdimensiongroupmember">isDimensionGroupMember</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.llmprompt">llmPrompt</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.sqlformula">sqlFormula</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="columnpropertiesinput.visibility">visibility</strong></td>
<td valign="top"><a href="#columnvisibility">ColumnVisibility</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionDetailsInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.bigquery">bigQuery</strong></td>
<td valign="top"><a href="#bigqueryconnectionconfiginput">BigQueryConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.connectiontype">connectionType</strong></td>
<td valign="top"><a href="#connectiontype">ConnectionType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.datasourcetype">dataSourceType</strong></td>
<td valign="top"><a href="#datasourcetype">DataSourceType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.databricks">databricks</strong></td>
<td valign="top"><a href="#databricksconnectionconfiginput">DatabricksConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.mysql">mysql</strong></td>
<td valign="top"><a href="#mysqlconnectionconfiginput">MySqlConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.postgres">postgres</strong></td>
<td valign="top"><a href="#postgresconnectionconfiginput">PostgresConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.redshift">redshift</strong></td>
<td valign="top"><a href="#redshiftconnectionconfiginput">RedshiftConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.snowflake">snowflake</strong></td>
<td valign="top"><a href="#snowflakeconnectionconfiginput">SnowflakeConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.sqlserver">sqlServer</strong></td>
<td valign="top"><a href="#sqlserverconnectionconfiginput">SqlServerConnectionConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="connectiondetailsinput.tableau">tableau</strong></td>
<td valign="top"><a href="#tableauconnectionconfiginput">TableauConnectionConfigInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ConversationFilterInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="conversationfilterinput.ids">ids</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="conversationfilterinput.ispinned">isPinned</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### DashboardInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardinput.id">id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardinput.sourcetype">sourceType</strong></td>
<td valign="top"><a href="#dashboardsourcetype">DashboardSourceType</a></td>
<td></td>
</tr>
</tbody>
</table>

### DashboardWidgetInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.body">body</strong></td>
<td valign="top"><a href="#updatechatmessagebodyoneof">UpdateChatMessageBodyOneOf</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.datarefreshedat">dataRefreshedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.id">id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.layout">layout</strong></td>
<td valign="top"><a href="#widgetlayoutinput">WidgetLayoutInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.markdowncontent">markdownContent</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.nlquery">nlQuery</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.sourceconversationid">sourceConversationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.sourcemessageid">sourceMessageId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.title">title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.visualizationid">visualizationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.visualizationtype">visualizationType</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dashboardwidgetinput.widgettype">widgetType</strong></td>
<td valign="top"><a href="#widgettype">WidgetType</a></td>
<td></td>
</tr>
</tbody>
</table>

### DatabricksConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfiginput.catalogfilters">catalogFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfiginput.clientid">clientId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfiginput.clientsecret">clientSecret</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfiginput.hostname">hostname</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="databricksconnectionconfiginput.httppath">httpPath</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.alias">alias</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.base">base</strong></td>
<td valign="top"><a href="#expressionbaseinput">ExpressionBaseInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.dateunit">dateUnit</strong></td>
<td valign="top"><a href="#dateunit">DateUnit</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.location">location</strong></td>
<td valign="top"><a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.properties">properties</strong></td>
<td valign="top"><a href="#columnpropertiesinput">ColumnPropertiesInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.tablename">tableName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframecolumninput.uniqueref">uniqueRef</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeExpressionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframeexpressioninput.flattened">flattened</strong></td>
<td valign="top">[<a href="#dataframesingleexpressiononeofinput">DataframeSingleExpressionOneOfInput</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeFunctionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframefunctioninput.argumentsindexes">argumentsIndexes</strong></td>
<td valign="top">[<a href="#int">Int</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframefunctioninput.type">type</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeLiteralInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframeliteralinput.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeRawExpressionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframerawexpressioninput.value">value</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DataframeSingleExpressionOneOfInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeofinput.column">column</strong></td>
<td valign="top"><a href="#dataframecolumninput">DataframeColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeofinput.function">function</strong></td>
<td valign="top"><a href="#dataframefunctioninput">DataframeFunctionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeofinput.literal">literal</strong></td>
<td valign="top"><a href="#dataframeliteralinput">DataframeLiteralInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeofinput.raw">raw</strong></td>
<td valign="top"><a href="#dataframerawexpressioninput">DataframeRawExpressionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesingleexpressiononeofinput.subquery">subquery</strong></td>
<td valign="top"><a href="#dataframesubqueryinput">DataframeSubqueryInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeSubqueryInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dataframesubqueryinput.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dataframesubqueryinput.rawcodecache">rawCodeCache</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### DeliveryConfigEmailInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deliveryconfigemailinput.to">to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DeliveryConfigSlackInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="deliveryconfigslackinput.channel">channel</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DerivedZSheetInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="derivedzsheetinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="derivedzsheetinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="derivedzsheetinput.schema">schema</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="derivedzsheetinput.sourcesql">sourceSql</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### DimensionColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="dimensioncolumninput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dimensioncolumninput.basedataframecolumn">baseDataframeColumn</strong></td>
<td valign="top"><a href="#basedataframecolumninput">BaseDataframeColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dimensioncolumninput.basetablecolumn">baseTableColumn</strong></td>
<td valign="top"><a href="#basetablecolumninput">BaseTableColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dimensioncolumninput.dateunit">dateUnit</strong></td>
<td valign="top"><a href="#dateunit">DateUnit</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="dimensioncolumninput.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### DrillDownInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="drilldowninput.drillfrom">drillFrom</strong></td>
<td valign="top"><a href="#dataframecolumninput">DataframeColumnInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="drilldowninput.drillto">drillTo</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### EditFilterMutation

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="editfiltermutation.filterid">filterId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="editfiltermutation.parsedfilteredit">parsedFilterEdit</strong></td>
<td valign="top"><a href="#parsedfiltereditinput">ParsedFilterEditInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ExpressionBaseInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="expressionbaseinput.zsheetref">zsheetRef</strong></td>
<td valign="top"><a href="#zsheetrefinput">ZSheetRefInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ExtractQuestionsFromTextInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="extractquestionsfromtextinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="extractquestionsfromtextinput.gcsfilekeys">gcsFileKeys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="extractquestionsfromtextinput.s3filekeys">s3FileKeys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="extractquestionsfromtextinput.text">text</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### FeedbackContent

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="feedbackcontent.item">item</strong></td>
<td valign="top"><a href="#feedbackcontentitem">FeedbackContentItem</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### FeedbackContentItem

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="feedbackcontentitem.feedback">feedback</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackcontentitem.feedbacktype">feedbackType</strong></td>
<td valign="top"><a href="#feedbacktype">FeedbackType</a></td>
<td></td>
</tr>
</tbody>
</table>

### FeedbackInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.containerid">containerId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.content">content</strong></td>
<td valign="top"><a href="#feedbackcontent">FeedbackContent</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.filejira">fileJira</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="feedbackinput.messageid">messageId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### FilterMutationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="filtermutationinput.add">add</strong></td>
<td valign="top">[<a href="#addparsedfiltermutation">AddParsedFilterMutation</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filtermutationinput.edit">edit</strong></td>
<td valign="top">[<a href="#editfiltermutation">EditFilterMutation</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="filtermutationinput.remove">remove</strong></td>
<td valign="top">[<a href="#removefiltermutation">RemoveFilterMutation</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### GetDomainPromptStringInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="getdomainpromptstringinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### InviteUsersInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="inviteusersinput.emails">emails</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="inviteusersinput.roleassignments">roleAssignments</strong></td>
<td valign="top">[<a href="#roleassignmentinput">RoleAssignmentInput</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### InviteUsersToDomainInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="inviteuserstodomaininput.domainid">domainId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="inviteuserstodomaininput.emails">emails</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="inviteuserstodomaininput.roleid">roleId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### LHSInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="lhsinput.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="lhsinput.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ListUsersInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="listusersinput.roleids">roleIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="listusersinput.scopes">scopes</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="listusersinput.search">search</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestioninput.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestioninput.source">source</strong></td>
<td valign="top"><a href="#mmsuggestionsource">MMSuggestionSource</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestioninput.status">status</strong></td>
<td valign="top"><a href="#mmsuggestionstatus">MMSuggestionStatus</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestioninput.task">task</strong></td>
<td valign="top"><a href="#mmsuggestiontaskinput">MMSuggestionTaskInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedFormulaInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.formuladescription">formulaDescription</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.formulaexpression">formulaExpression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.formulaname">formulaName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedformulainput.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedKnowledgeInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledgeinput.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledgeinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledgeinput.knowledgestr">knowledgeStr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedknowledgeinput.messageid">messageId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskAddLearnedMetricInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetricinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetricinput.metricdescription">metricDescription</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetricinput.metricexpression">metricExpression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskaddlearnedmetricinput.metricname">metricName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskColumnDescriptionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescriptioninput.columnname">columnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescriptioninput.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescriptioninput.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumndescriptioninput.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskColumnNamesInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnamesinput.explanation">explanation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnamesinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnamesinput.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskcolumnnamesinput.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.addcolumndescription">addColumnDescription</strong></td>
<td valign="top"><a href="#mmsuggestiontaskcolumndescriptioninput">MMSuggestionTaskColumnDescriptionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.addlearnedformula">addLearnedFormula</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedformulainput">MMSuggestionTaskAddLearnedFormulaInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.addlearnedknowledge">addLearnedKnowledge</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedknowledgeinput">MMSuggestionTaskAddLearnedKnowledgeInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.addlearnedmetric">addLearnedMetric</strong></td>
<td valign="top"><a href="#mmsuggestiontaskaddlearnedmetricinput">MMSuggestionTaskAddLearnedMetricInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.addmissingjoin">addMissingJoin</strong></td>
<td valign="top"><a href="#mmsuggestiontaskjoininput">MMSuggestionTaskJoinInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.clarifycolumnnames">clarifyColumnNames</strong></td>
<td valign="top"><a href="#mmsuggestiontaskcolumnnamesinput">MMSuggestionTaskColumnNamesInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.entertabledescription">enterTableDescription</strong></td>
<td valign="top"><a href="#mmsuggestiontasktabledescriptioninput">MMSuggestionTaskTableDescriptionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskinput.type">type</strong></td>
<td valign="top"><a href="#mmsuggestiontasktype">MMSuggestionTaskType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskJoinInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoininput.leftcolumnname">leftColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoininput.leftsourceid">leftSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoininput.relationshiptype">relationshipType</strong></td>
<td valign="top"><a href="#zsheetrelationshiptype">ZSheetRelationshipType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoininput.rightcolumnname">rightColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontaskjoininput.rightsourceid">rightSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskTableDescriptionInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontasktabledescriptioninput.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontasktabledescriptioninput.sourceid">sourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mmsuggestiontasktabledescriptioninput.sourcename">sourceName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### MeasureColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="measurecolumninput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measurecolumninput.basedataframecolumn">baseDataframeColumn</strong></td>
<td valign="top"><a href="#basedataframecolumninput">BaseDataframeColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measurecolumninput.basetablecolumn">baseTableColumn</strong></td>
<td valign="top"><a href="#basetablecolumninput">BaseTableColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measurecolumninput.dateunit">dateUnit</strong></td>
<td valign="top"><a href="#dateunit">DateUnit</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="measurecolumninput.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### MySqlConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfiginput.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfiginput.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfiginput.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="mysqlconnectionconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PaginationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="paginationinput.pageindex">pageIndex</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="paginationinput.pagesize">pageSize</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ParsedFilterEditInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="parsedfiltereditinput.operator">operator</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfiltereditinput.orgroupmutation">orGroupMutation</strong></td>
<td valign="top"><a href="#filtermutationinput">FilterMutationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfiltereditinput.rhs">rhs</strong></td>
<td valign="top"><a href="#rhsinput">RHSInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ParsedFilterInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterinput.lhs">lhs</strong></td>
<td valign="top"><a href="#lhsinput">LHSInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterinput.operator">operator</strong></td>
<td valign="top"><a href="#dataframefunctiontype">DataframeFunctionType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="parsedfilterinput.rhs">rhs</strong></td>
<td valign="top"><a href="#rhsinput">RHSInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PlaybookInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="playbookinput.domainid">domainId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbookinput.id">id</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbookinput.markdown">markdown</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbookinput.title">title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### PlaybookUpdateInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="playbookupdateinput.body">body</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="playbookupdateinput.playbookid">playbookId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### PostgresConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfiginput.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfiginput.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfiginput.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="postgresconnectionconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvDomainCreateInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processcsvdomaincreateinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvdomaincreateinput.domainname">domainName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvDomainReuseInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processcsvdomainreuseinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvdomainreuseinput.tableid">tableId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvdomainreuseinput.tableoperation">tableOperation</strong></td>
<td valign="top"><a href="#processcsvtableoperation">ProcessCsvTableOperation</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvRequestInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processcsvrequestinput.csvkey">csvKey</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvrequestinput.csvname">csvName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvrequestinput.domaincreate">domainCreate</strong></td>
<td valign="top"><a href="#processcsvdomaincreateinput">ProcessCsvDomainCreateInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvrequestinput.domainoperation">domainOperation</strong></td>
<td valign="top"><a href="#processcsvdomainoperation">ProcessCsvDomainOperation</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processcsvrequestinput.domainreuse">domainReuse</strong></td>
<td valign="top"><a href="#processcsvdomainreuseinput">ProcessCsvDomainReuseInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ProcessLookerFileUploadInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processlookerfileuploadinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processlookerfileuploadinput.lookergcskeys">lookerGCSKeys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processlookerfileuploadinput.lookers3keys">lookerS3Keys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### ProcessTableauFileUploadInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="processtableaufileuploadinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processtableaufileuploadinput.tableaugcskeys">tableauGCSKeys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="processtableaufileuploadinput.tableaus3keys">tableauS3Keys</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### PromptSQLPairInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="promptsqlpairinput.prompt">prompt</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="promptsqlpairinput.sql">sql</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ProxyConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfiginput.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfiginput.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="proxyconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItemPatch

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitempatch.action">action</strong></td>
<td valign="top"><a href="#questionbankitemaction">QuestionBankItemAction</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitempatch.code">code</strong></td>
<td valign="top"><a href="#codeinput">CodeInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitempatch.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitempatch.question">question</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitempatch.sourcedetails">sourceDetails</strong></td>
<td valign="top"><a href="#questionbankitemsourcedetailsinput">QuestionBankItemSourceDetailsInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItemSourceDetailsInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsourcedetailsinput.conversationid">conversationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionbankitemsourcedetailsinput.messageid">messageId</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### QuestionsFiltersInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="questionsfiltersinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionsfiltersinput.endtime">endTime</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionsfiltersinput.starttime">startTime</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="questionsfiltersinput.userid">userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### RHSInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhsinput.literal">literal</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsinput.range">range</strong></td>
<td valign="top"><a href="#rhsrangeinput">RHSRangeInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsinput.set">set</strong></td>
<td valign="top"><a href="#rhssetinput">RHSSetInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### RHSRangeInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhsrangeinput.closed">closed</strong></td>
<td valign="top"><a href="#intervalclosed">IntervalClosed</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsrangeinput.end">end</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="rhsrangeinput.start">start</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RHSSetInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="rhssetinput.values">values</strong></td>
<td valign="top">[<a href="#dataframeexpressioninput">DataframeExpressionInput</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### RedshiftConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfiginput.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfiginput.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfiginput.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="redshiftconnectionconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RemoveColumnMutationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="removecolumnmutationinput.column">column</strong></td>
<td valign="top"><a href="#dataframecolumninput">DataframeColumnInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RemoveFilterMutation

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="removefiltermutation.filterid">filterId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RoleAssigmentsInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="roleassigmentsinput.scope">scope</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### RoleAssignmentInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="roleassignmentinput.roleid">roleId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="roleassignmentinput.scopes">scopes</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### SaveDerivedFieldInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.code">code</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.domainid">domainId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.expression">expression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="savederivedfieldinput.sourcezsheetref">sourceZSheetRef</strong></td>
<td valign="top"><a href="#zsheetrefinput">ZSheetRefInput</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleDeliveryInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduledeliveryinput.emailconfig">emailConfig</strong></td>
<td valign="top"><a href="#deliveryconfigemailinput">DeliveryConfigEmailInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduledeliveryinput.slackconfig">slackConfig</strong></td>
<td valign="top"><a href="#deliveryconfigslackinput">DeliveryConfigSlackInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduledeliveryinput.type">type</strong></td>
<td valign="top"><a href="#deliverytype">DeliveryType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleTaskInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduletaskinput.delivery">delivery</strong></td>
<td valign="top"><a href="#scheduledeliveryinput">ScheduleDeliveryInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletaskinput.resourceid">resourceId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletaskinput.type">type</strong></td>
<td valign="top"><a href="#scheduletasktype">ScheduleTaskType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleTimingInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scheduletiminginput.intervalinmins">intervalInMins</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scheduletiminginput.starttime">startTime</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ScopeRoleAssignmentInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="scoperoleassignmentinput.principalid">principalId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="scoperoleassignmentinput.roleid">roleId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SnowflakeConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.account">account</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.privatekey">privateKey</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.proxyconfig">proxyConfig</strong></td>
<td valign="top"><a href="#proxyconfiginput">ProxyConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.role">role</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.user">user</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="snowflakeconnectionconfiginput.warehouse">warehouse</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SortColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumninput.column">column</strong></td>
<td valign="top"><a href="#dataframecolumninput">DataframeColumnInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sortcolumninput.order">order</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SqlServerConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfiginput.databasefilters">databaseFilters</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfiginput.host">host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfiginput.port">port</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="sqlserverconnectionconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### StructuredQuery

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="structuredquery.pieces">pieces</strong></td>
<td valign="top">[<a href="#structuredquerypieceinput">StructuredQueryPieceInput</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### StructuredQueryPieceInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.action">action</strong></td>
<td valign="top"><a href="#refinementactiontype">RefinementActionType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.column">column</strong></td>
<td valign="top"><a href="#dataframecolumninput">DataframeColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.expression">expression</strong></td>
<td valign="top"><a href="#dataframeexpressioninput">DataframeExpressionInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.playgroundqueryhint">playgroundQueryHint</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.referredmessageid">referredMessageId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.text">text</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="structuredquerypieceinput.vizreference">vizReference</strong></td>
<td valign="top"><a href="#vizreferenceinput">VizReferenceInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### SubscriptionAuthInput

The subscription type defines how to listen to specific events from the backend. We use it to
stream parts of the chat messages.

Authentication for subscription requires AuthInput to be passed in the payload.

It's checked here on app-server side: javascript/packages/app-server/src/context.ts
And added here on frontend side: javascript/packages/frontend/util/subscribeAuthneticated.ts

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="subscriptionauthinput.token">token</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### TableauConnectionConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="tableauconnectionconfiginput.password">password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="tableauconnectionconfiginput.username">username</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ToolSelection

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="toolselection.optintoolnames">optInToolNames</strong></td>
<td valign="top">[<a href="#chattoolname">ChatToolName</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### UnassignRoleInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="unassignroleinput.principalids">principalIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unassignroleinput.roleid">roleId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unassignroleinput.scopes">scopes</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### UnstructuredIndexPropertiesInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexpropertiesinput.embedmetadatacolumns">embedMetadataColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexpropertiesinput.indexmetadatafacets">indexMetadataFacets</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexpropertiesinput.promptmetadatacolumns">promptMetadataColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexpropertiesinput.searchoutputcolumns">searchOutputColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="unstructuredindexpropertiesinput.shouldembed">shouldEmbed</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### UpdateChatMessageBodyOneOf

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.addcolumn">addColumn</strong></td>
<td valign="top"><a href="#addcolumnmutationinput">AddColumnMutationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.drilldown">drillDown</strong></td>
<td valign="top"><a href="#drilldowninput">DrillDownInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.filtermutations">filterMutations</strong></td>
<td valign="top"><a href="#filtermutationinput">FilterMutationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.noop">noop</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.playbookupdate">playbookUpdate</strong></td>
<td valign="top"><a href="#playbookupdateinput">PlaybookUpdateInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.removecolumn">removeColumn</strong></td>
<td valign="top"><a href="#removecolumnmutationinput">RemoveColumnMutationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.sql">sql</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.visualization">visualization</strong></td>
<td valign="top"><a href="#visualizationinput">VisualizationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updatechatmessagebodyoneof.vizeditorupdate">vizEditorUpdate</strong></td>
<td valign="top"><a href="#vizeditorupdateinput">VizEditorUpdateInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### UpdateEvaluationRunInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="updateevaluationruninput.gtsql">gtSQL</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updateevaluationruninput.manualfeedback">manualFeedback</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updateevaluationruninput.manualscore">manualScore</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updateevaluationruninput.promptindex">promptIndex</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="updateevaluationruninput.sessionindex">sessionIndex</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### VisualizationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.columnorder">columnOrder</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.columns">columns</strong></td>
<td valign="top">[<a href="#dataframecolumninput">DataframeColumnInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.id">id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.pagination">pagination</strong></td>
<td valign="top"><a href="#paginationinput">PaginationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.title">title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="visualizationinput.type">type</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a></td>
<td></td>
</tr>
</tbody>
</table>

### VizConfigInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="vizconfiginput.alwaysusecompactnumberformat">alwaysUseCompactNumberFormat</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizconfiginput.openshowdatapanelbydefault">openShowDataPanelByDefault</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### VizEditorUpdateInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="vizeditorupdateinput.dimensions">dimensions</strong></td>
<td valign="top">[<a href="#dimensioncolumninput">DimensionColumnInput</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizeditorupdateinput.measures">measures</strong></td>
<td valign="top">[<a href="#measurecolumninput">MeasureColumnInput</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizeditorupdateinput.tabledisplayorder">tableDisplayOrder</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizeditorupdateinput.viztype">vizType</strong></td>
<td valign="top"><a href="#visualizationtype">VisualizationType</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### VizReferenceInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="vizreferenceinput.charttype">chartType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreferenceinput.dataframecollectedatms">dataframeCollectedAtMs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreferenceinput.dataframeid">dataframeId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="vizreferenceinput.hidden">hidden</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### WidgetLayoutInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayoutinput.height">height</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayoutinput.left">left</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayoutinput.top">top</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="widgetlayoutinput.width">width</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnBulkInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnbulkinput.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnbulkinput.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnFilterInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnfilterinput.isaggregated">isAggregated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnfilterinput.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.aliases">aliases</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.contenttag">contentTag</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.defaultorder">defaultOrder</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.format">format</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.isprimarykey">isPrimaryKey</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.prioritized">prioritized</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.skipner">skipNer</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.unstructuredindexproperties">unstructuredIndexProperties</strong></td>
<td valign="top"><a href="#unstructuredindexpropertiesinput">UnstructuredIndexPropertiesInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.useridentificationinfo">userIdentificationInfo</strong></td>
<td valign="top"><a href="#useridentificationinfo">UserIdentificationInfo</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumninput.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnLocationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocationinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocationinput.zsheetalias">zsheetAlias</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnlocationinput.zsheetref">zsheetRef</strong></td>
<td valign="top"><a href="#zsheetrefinput">ZSheetRefInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnOrder

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnorder.direction">direction</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetcolumnorder.field">field</strong></td>
<td valign="top"><a href="#zsheetcolumnorderfield">ZSheetColumnOrderField</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDefaultOrderByInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdefaultorderbyinput.column">column</strong></td>
<td valign="top"><a href="#zsheetentitycolumninput">ZSheetEntityColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetdefaultorderbyinput.order">order</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedFieldBulkInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldbulkinput.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldbulkinput.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedFieldInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.aggregationtype">aggregationType</strong></td>
<td valign="top"><a href="#zsheetcolumnaggregationtype">ZSheetColumnAggregationType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.aliases">aliases</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.allowedvalues">allowedValues</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.areenumvaluesordered">areEnumValuesOrdered</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.contenttag">contentTag</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.datatype">dataType</strong></td>
<td valign="top"><a href="#zsheetcolumndatatype">ZSheetColumnDataType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.datecolumnname">dateColumnName</strong></td>
<td valign="top"><a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.defaultorder">defaultOrder</strong></td>
<td valign="top"><a href="#sortdirection">SortDirection</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.displayformat">displayFormat</strong></td>
<td valign="top"><a href="#displayformat">DisplayFormat</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.displayname">displayName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.expression">expression</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.format">format</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.formulatype">formulaType</strong></td>
<td valign="top"><a href="#formulatype">FormulaType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.groupbycolumns">groupByColumns</strong></td>
<td valign="top">[<a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.isprimarykey">isPrimaryKey</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.llmprompt">llmPrompt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.location">location</strong></td>
<td valign="top"><a href="#zsheetderivedfieldlocationinput">ZSheetDerivedFieldLocationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.nermode">nerMode</strong></td>
<td valign="top"><a href="#nermode">NerMode</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.prioritized">prioritized</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.unstructuredindexproperties">unstructuredIndexProperties</strong></td>
<td valign="top"><a href="#unstructuredindexpropertiesinput">UnstructuredIndexPropertiesInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.useridentificationinfo">userIdentificationInfo</strong></td>
<td valign="top"><a href="#useridentificationinfo">UserIdentificationInfo</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldinput.visibility">visibility</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetDerivedFieldLocationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldlocationinput.zsheetid">zSheetId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetderivedfieldlocationinput.zsheetname">zSheetName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityColumnInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumninput.location">location</strong></td>
<td valign="top"><a href="#zsheetcolumnlocationinput">ZSheetColumnLocationInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumninput.wildcardcolumn">wildcardColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumninput">ZSheetEntityColumnInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentitycolumninput.wildcardedurl">wildcardedUrl</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetEntityInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.defaultcolumns">defaultColumns</strong></td>
<td valign="top">[<a href="#zsheetentitycolumninput">ZSheetEntityColumnInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.defaultorderby">defaultOrderBy</strong></td>
<td valign="top"><a href="#zsheetdefaultorderbyinput">ZSheetDefaultOrderByInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.idcolumn">idColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumninput">ZSheetEntityColumnInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.namecolumn">nameColumn</strong></td>
<td valign="top"><a href="#zsheetentitycolumninput">ZSheetEntityColumnInput</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetentityinput.templateid">templateID</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.codegenconfig">codegenConfig</strong></td>
<td valign="top"><a href="#codegenconfiginput">CodegenConfigInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.description">description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.domainsysteminstructions">domainSystemInstructions</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.hiddensourceids">hiddenSourceIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.joins">joins</strong></td>
<td valign="top">[<a href="#zsheetjoininput">ZSheetJoinInput</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.location">location</strong></td>
<td valign="top"><a href="#zsheetlocationinput">ZSheetLocationInput</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.sourceids">sourceIds</strong></td>
<td valign="top">[<a href="#id">ID</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.type">type</strong></td>
<td valign="top"><a href="#zsheettype">ZSheetType</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetinput.vizconfig">vizConfig</strong></td>
<td valign="top"><a href="#vizconfiginput">VizConfigInput</a></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetJoinInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoininput.leftcolumnname">leftColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoininput.leftsourceid">leftSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoininput.relationshiptype">relationshipType</strong></td>
<td valign="top"><a href="#zsheetrelationshiptype">ZSheetRelationshipType</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoininput.rightcolumnname">rightColumnName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetjoininput.rightsourceid">rightSourceId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetLocationInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocationinput.connectionid">connectionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetlocationinput.database">database</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetRefInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetrefinput.name">name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong id="zsheetrefinput.uuid">uuid</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetsFilterInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="zsheetsfilterinput.type">type</strong></td>
<td valign="top">[<a href="#zsheettype">ZSheetType</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

## Enums

### AmbiguityEgregiousness

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>AMBIGUITY_EGREGIOUSNESS_HIGH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>AMBIGUITY_EGREGIOUSNESS_LOW</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>AMBIGUITY_EGREGIOUSNESS_MEDIUM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>AMBIGUITY_EGREGIOUSNESS_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### AuthType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SAML</strong></td>
<td></td>
</tr>
</tbody>
</table>

### BucketType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>GCS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>S3</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ChatMessageSender

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ASSISTANT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SYSTEM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>USER</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ChatToolName

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DOMAIN_SETUP</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PLAYBOOK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PYTHON_INTERPRETER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TABULAR_DATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TEXTUAL_DATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNSPECIFIED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ChatToolType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ADMIN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>BETA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>REGULAR</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ColumnVisibility

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ALWAYS_DISPLAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>HIDDEN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NEVER_DISPLAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>POPULARITY_BASED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionSyncStatus

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CONNECTION_SYNC_STATUS_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FAILED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUEUED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>RUNNING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SUCCESS</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>BIGQUERY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CONNECTION_TYPE_UNSPECIFIED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATABRICKS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MYSQL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>POSTGRES</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>REDSHIFT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SNOWFLAKE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SQL_SERVER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TABLEAU</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ConversationType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CANVAS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CHAT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN_CONVERSATION_TYPE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DashboardScope

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>EDITOR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VIEWER</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DashboardSourceType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DASHBOARD_TYPE_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>LOOKER_IMPORTED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TABLEAU_IMPORTED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>USER_CREATED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WISDOM_GENERATED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DashboardSummaryType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>SIMPLE_SUMMARY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WHAT_CHANGED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DataSourceType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>BI_TOOL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATA_SOURCE_TYPE_UNSPECIFIED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WAREHOUSE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeFunctionType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>FUNC_ADD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ALIAS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ALL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_AND</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ANY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_AVG</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_AVG_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_BETWEEN_DURATION_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CASE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CASE_ELSE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CAST</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CAST_TIMEZONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_COALESCE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CONCATENATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_COUNT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_COUNT_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_COUNT_IF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_DATETIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_TIMESTAMP</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_CURRENT_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATEADD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATEDIFF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATESUB</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATETIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATETIME_ADD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATETIME_DIFF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATETIME_SUB</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATETIME_TRUNC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DATE_FROM_PARTS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DAY_PART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DENSE_RANK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DIV</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DURATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DURATION_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_DURATION_WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_EQ</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_EXISTS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_EXPLODE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_EXTRACT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_GROUNDED_DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_GT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_GTE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_IF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ILIKE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_IN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_IN_THIS_PERIOD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_IS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LENGTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LIKE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LOWER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LTE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_LTRIM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MAX</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MAX_BY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MIN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MIN_BY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MONTH_PART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_MUL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEG</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEQ</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_DAYS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_FISCAL_QUARTERS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_FISCAL_YEARS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_MONTHS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_QUARTERS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_WEEKS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NEXT_N_YEARS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NOT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NOW</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NULLIF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NULL_SAFE_EQ</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_NULL_SAFE_NEQ</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_OR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ORDER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ORDERED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PARTITION_BY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_DAYS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_FISCAL_QUARTERS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_FISCAL_YEARS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_MONTHS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_QUARTERS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_WEEKS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_PREVIOUS_N_YEARS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_QUARTER_PART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RANK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RELATIVE_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ROUND</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_ROW_NUMBER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_RTRIM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_SAFEDIV</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_STAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_SUB</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_SUBSTRING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_SUM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_SUM_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TIMESTAMP</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TIMESTAMP_ADD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TIMESTAMP_DIFF</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TIMESTAMP_SUB</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TIMESTAMP_TRUNC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TRIM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TRUNCATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TRYCAST</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_TUPLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_UNNEST</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_UPPER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WEEK_PART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WINDOW</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WINDOW_FRAME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WISDOM_CURRENT_DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WISDOM_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_WISDOM_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNC_YEAR_PART</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DataframeSourceType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>BASE_TABLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CTE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DERIVED_TABLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DateUnit

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DAYOFWEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DAYOFYEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>EPOCH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>HOUR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MINUTE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NO_UNIT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SECOND</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WEEK</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>YEAR</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DeliveryType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>EMAIL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SLACK</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DerivedFieldType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>FIELD_FORMULA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FIELD_LOD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FIELD_MEASURE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FIELD_UNKNOWN_TYPE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DescopeRole

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>SUPER_USER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### DisplayFormat

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DATE_DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_DATETIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_DAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_FISCAL_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_FISCAL_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_MONTH</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_QUARTER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_TIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE_YEAR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DISPLAY_FORMAT_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_DAYS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_HOURS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_MINUTES</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_MONTHS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_QUARTERS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_SECONDS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_WEEKS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DURATION_YEARS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>LOCATION_COUNTRY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>LOCATION_STATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NUMBER_CURRENCY_USD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NUMBER_DECIMAL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NUMBER_INTEGER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NUMBER_PERCENTAGE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### FeedbackType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NEGATIVE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NEUTRAL</strong> ⚠️</td>
<td>
<p>⚠️ <strong>DEPRECATED</strong></p>
<blockquote>

Use null instead

</blockquote>
</td>
</tr>
<tr>
<td valign="top"><strong>POSITIVE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### FieldDataType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DIMENSION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MEASURE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### FieldSourceType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>LLM_GENERATED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PREDEFINED_COLUMN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PREDEFINED_FORMULA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PREDEFINED_MEASURE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### FormulaType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>LLM_FUNCTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SQL</strong></td>
<td></td>
</tr>
</tbody>
</table>

### IntervalClosed

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>BOTH_INTERVALS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>LEFT_INTERVAL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NEITHER_INTERVAL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>RIGHT_INTERVAL</strong></td>
<td></td>
</tr>
</tbody>
</table>

### JobStatus

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>JOB_STATUS_FAILED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>JOB_STATUS_QUEUED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>JOB_STATUS_RUNNING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>JOB_STATUS_SUCCESS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>JOB_STATUS_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### LLMModelComponent

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DEFAULT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANUAL_SELECTION_4O</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANUAL_SELECTION_4O_MINI</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANUAL_SELECTION_O1</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANUAL_SELECTION_O1_MINI</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANUAL_SELECTION_O3_MINI</strong></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionSource

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_CONVERSATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_IMPORT_LOOKER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_IMPORT_TABLEAU</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_MODEL_DERIVED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_ONBOARDING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_SOURCE_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionStatus

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>MM_SUGGESTION_STATUS_ACCEPTED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_STATUS_DECLINED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_STATUS_PENDING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MM_SUGGESTION_STATUS_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### MMSuggestionTaskType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ADD_COLUMN_DESCRIPTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ADD_LEARNED_FORMULA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ADD_LEARNED_KNOWLEDGE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ADD_LEARNED_METRIC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ADD_MISSING_JOINS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CLARIFY_COLUMN_NAMES</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ENTER_TABLE_DESCRIPTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SHOW_TEXT_SUGGESTIONS</strong></td>
<td></td>
</tr>
</tbody>
</table>

### MetadataStepScope

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ALL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CACHE_HIT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CODE_EXECUTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CODE_GENERATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ENTITY_EXTRACTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>GRAIN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MODEL_SELECTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>REFINEMENT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VISUALIZATION_SELECTION</strong></td>
<td></td>
</tr>
</tbody>
</table>

### NerMode

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NER_DISABLED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NER_ENABLED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NER_NOT_APPLICABLE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### OnboardingFeature

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHART_PICKER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CHAT_SEARCH_PAGE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FILTERS</strong></td>
<td></td>
</tr>
</tbody>
</table>

### OnboardingPreference

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>OWN_DATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SAMPLE_DATA</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvDomainOperation

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CREATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>REUSE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ProcessCsvTableOperation

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CSV_TABLE_OPERATION_APPEND</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CSV_TABLE_OPERATION_CREATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CSV_TABLE_OPERATION_REPLACE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>CSV_TABLE_OPERATION_UNSPECIFIED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### QueryIntentionType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>QUERY_INTENTION_ASK_LLM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUERY_INTENTION_GET_DATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUERY_INTENTION_GET_METADATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUERY_INTENTION_UNINTENDED_QUESTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUERY_INTENTION_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### QuestionBankItemAction

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>QUESTION_BANK_ITEM_ACTION_INVALIDATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUESTION_BANK_ITEM_ACTION_UNSPECIFIED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>QUESTION_BANK_ITEM_ACTION_VALIDATE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### RefinementActionType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NO_ACTION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ROOT_CAUSE_ANALYSIS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SEARCH</strong></td>
<td></td>
</tr>
</tbody>
</table>

### RoleDepartment

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DATA</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ENGINEERING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FINANCE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>GTM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>REVENUE</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ScheduleTaskType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CONVERSATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DASHBOARD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PLAYBOOK</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ScopeType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CONVERSATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DASHBOARD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DOMAIN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### SortDirection

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ASC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DESC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### StatusCode

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ERROR</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NOT_FOUND</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>OK</strong></td>
<td></td>
</tr>
</tbody>
</table>

### TrialExtensionReason

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>GRACE_PERIOD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>INVITED_ANOTHER_USER</strong></td>
<td></td>
</tr>
</tbody>
</table>

### UserIdentificationInfo

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NO_USER_IDENTIFICATION_INFO</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>USER_EMAIL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>USER_FULL_NAME</strong></td>
<td></td>
</tr>
</tbody>
</table>

### UserStateNamespace

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>EVALUATION</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ONBOARDING</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>USER_PREFERENCES</strong></td>
<td></td>
</tr>
</tbody>
</table>

### VerifiedCodeUsageType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>VERIFIED_CODE_USAGE_NOT_USED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VERIFIED_CODE_USAGE_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VERIFIED_CODE_USAGE_USED</strong></td>
<td></td>
</tr>
</tbody>
</table>

### VisualizationType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>AREA_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>BAR_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>COLUMN_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>COUNTRY_MAP_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FORECAST_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FUNNEL_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>GROUPED_BAR_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>GROUPED_COLUMN_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>HEATMAP_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>LINE_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PIE_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>POLAR_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SANKEY_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SCATTER_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SPIDER_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STACKED_100_BAR_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STACKED_100_COLUMN_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STACKED_AREA_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STACKED_BAR_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STACKED_COLUMN_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>STATE_MAP_CHART</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TABLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TEXT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>UNKNOWN_VISUALIZATION</strong></td>
<td></td>
</tr>
</tbody>
</table>

### WidgetType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>WIDGET_TYPE_MARKDOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WIDGET_TYPE_SUMMARY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WIDGET_TYPE_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>WIDGET_TYPE_VISUALIZATION</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnAggregationType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>AVERAGE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>AVERAGE_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>COUNT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>COUNT_DISTINCT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MAX</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MIN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SUM</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SUM_DISTINCT</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnDataType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ARRAY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>BIGNUMERIC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>BINARY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>BOOL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>COLUMNDATATYPE_UNKNOWN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DATETIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DOUBLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>FLOAT</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>INT32</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>INT64</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>JSON</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NULL</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>RECORD</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>SUPER</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TIME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>TIMESTAMP</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VARCHAR</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetColumnOrderField

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>FOREIGN_KEY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NAME</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>PRIMARY_KEY</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetNullValueOrder

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>NULLS_FIRST_ALWAYS</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NULLS_FIRST_ASC_LAST_DESC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NULLS_FIRST_DESC_LAST_ASC</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>NULLS_LAST_ALWAYS</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetRelationshipType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>MANY_TO_MANY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MANY_TO_ONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ONE_TO_MANY</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ONE_TO_ONE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>RELATIONSHIP_TYPE_UNKNOWN</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetTableType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>BASE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DERIVED</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>MATERIALIZED_VIEW</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VIEW</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>VIRTUAL</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ZSheetType

<table>
<thead>
<tr>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>DATASET_TABLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DERIVED_TABLE</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>DOMAIN</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ENHANCED_ZSHEET</strong> ⚠️</td>
<td>
<p>⚠️ <strong>DEPRECATED</strong></p>
<blockquote>

Only use this field by the old ZSheet pages

</blockquote>
</td>
</tr>
<tr>
<td valign="top"><strong>TABLE</strong></td>
<td></td>
</tr>
</tbody>
</table>

## Scalars

### BigInt

### Boolean

The `Boolean` scalar type represents `true` or `false`.

### DateTime

### Float

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

### Int

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### JSON

### String

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

## Interfaces

### Node

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong id="node.id">id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td></td>
</tr>
</tbody>
</table>

**Possible Types:** [ChatConversation](#chatconversation), [ChatMessage](#chatmessage), [ChatMessageExplanation](#chatmessageexplanation), [ChatMessageGeneratedCode](#chatmessagegeneratedcode), [ChatMessageGeneratedNLExplanation](#chatmessagegeneratednlexplanation), [ChatMessageMetadata](#chatmessagemetadata), [ChatMessageTrainingModeInfo](#chatmessagetrainingmodeinfo), [ChatQuestion](#chatquestion), [ConversationMessageCount](#conversationmessagecount), [Dashboard](#dashboard), [DashboardWidget](#dashboardwidget), [QuestionBankItem](#questionbankitem), [Schedule](#schedule), [User](#user), [ZSheet](#zsheet)

## Unions

### ColumnDetails

<table>
<thead>
<tr>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong><a href="#datetimedetails">DateTimeDetails</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#nulldetails">NullDetails</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#numericdetails">NumericDetails</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#stringdetails">StringDetails</a></strong></td>
<td></td>
</tr>
</tbody>
</table>

### ConnectionConfig

<table>
<thead>
<tr>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong><a href="#bigqueryconnectionconfig">BigQueryConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#databricksconnectionconfig">DatabricksConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#mysqlconnectionconfig">MySqlConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#redshiftconnectionconfig">RedshiftConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#snowflakeconnectionconfig">SnowflakeConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#sqlserverconnectionconfig">SqlServerConnectionConfig</a></strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong><a href="#tableauconnectionconfig">TableauConnectionConfig</a></strong></td>
<td></td>
</tr>
</tbody>
</table>

<!-- END graphql-markdown -->


---

© 2025 Wisdom API. All rights reserved.