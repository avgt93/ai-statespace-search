/* eslint-disable react-hooks/rules-of-hooks */
/* eslint-disable react/prop-types */

/* eslint-disable no-unused-vars */
import { useState } from "react";
import { Game } from "../src/Game.js";
import { State } from "../src/Game.js";
import { parse, stringify } from "flatted";
import { searchResults } from "../src/Search.js";
import Node from "./Node.jsx";
import "./App.css";
import { GameState } from "./config.js";

let data = parse(stringify(searchResults));
console.log(data);
let node = data.parent;
let startState = new State(3, 3, false);
while (node.parent != null) {
	node = node.parent;
}

const useDataParser = (d) => {
	const [data, setData] = useState({
		gameStatus: d.data.gameStatus,
		movePerformed: d.data.movePerformed
			? `Missionaries:${d.data.movePerformed.missionaries}, Cannibals:${d.data.movePerformed.cannibals}`
			: "No move performed",
		state: d.data.state
			? `Missionaries:${d.data.state.missionaries},Cannibals:${d.data.state.cannibals},Boat:${d.data.state.boat}`
			: "No state",
	});

	// console.log(d);
	return data;
};

const TreeNode = ({ node, depth }) => {
	return (
		<div className="tree-node">
			{node.children.map((child, idx) => {
				const childData = useDataParser(child);
				return (
					<div key={idx}>
						<Node childData={childData} />
						{child.children.length > 0 &&
							{
								/* <TreeNode node={child} depth={depth + 1} /> */
							}}
					</div>
				);
			})}
		</div>
	);
};

const App = () => {
	return (
		<div className="App">
			<h1>Game Search Tree</h1>
			<TreeNode node={node} />
		</div>
	);
};

export default App;
