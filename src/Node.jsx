import React from "react";
import "./node.css";

function Node(childData) {
	return (
		<div className="node_root">
			<p>
				gameStatus: {childData.gameStatus}, movePerformed:{" "}
				{childData.movePerformed}, state: {childData.state}
			</p>
		</div>
	);
}

export default Node;
