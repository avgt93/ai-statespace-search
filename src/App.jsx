/* eslint-disable react-hooks/rules-of-hooks */
/* eslint-disable react/prop-types */

/* eslint-disable no-unused-vars */
import { useState } from "react";
import Tree from "react-d3-tree";
import { Game } from "../src/Game.js";
import { State } from "../src/Game.js";
import { parse, stringify } from "flatted";
import { searchResults } from "../src/Search.js";
import Node from "./Node.jsx";
import "./App.css";
import { GameState } from "./config.js";

let data = parse(stringify(searchResults));
console.log(data);

const useDataParser = (d) => {
	const [data, setData] = useState({
		gameStatus: d.data.gameStatus,
		movePerformed: d.data.movePerformed
			? `${d.data.movePerformed.missionaries},${d.data.movePerformed.cannibals}`
			: "Null",
		state: d.data.state
			? `${d.data.state.missionaries},${d.data.state.cannibals},${d.data.state.boat}`
			: "Null",
	});
	return data;
};

const TreeNode = ({ node, depth }) => {
	console.log(node);

	return (
		<div className="tree-node">
			{node.children.length > 0 &&
				node.data.gameStatus === GameState.Running &&
				node.children.map((child, idx) => {
					let childData = useDataParser(child);
					return (
						<div key={idx} className=".node_level">
							{/* <Node
								gameStatus={childData.gameStatus}
								movePerformed={childData.movePerformed}
								state={childData.state}
							/> */}
							{/* {!(child.gameStatus === GameState.Failed) &&
								child.children.length > 0 && (
									<TreeNode node={child} depth={depth + 1} />
								)} */}
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
			{/* <Tree data={data} />
			 */}
			<Node />
		</div>
	);
};

export default App;
