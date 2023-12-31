import { searchResults } from "./game/Search";
import { ArcherContainer, ArcherElement } from "react-archer";
import "./styles/Node.css";

const results = searchResults;
console.log(results);
results.data.display();

export default function Node(node) {
	if (node.length === 0) return null;
	const className = "node";

	if (node.children.length === 0) {
		return (
			<ArcherContainer strokeColor="black" noCurves={false} offset={2}>
				{node.children.map((child, index) => (
					<div className="node" key={index}>
						<ArcherElement
							id="start"
							relations={[
								{
									targetId: `element${index}`,
									targetAnchor: "top",
									sourceAnchor: "bottom",
									style: { strokeColor: "gray", strokeWidth: 1 },
									label: `${child.data.movePerformed}`,
								},
							]}
						>
							{child.data.gameStatus === "won"
								? className.concat(" won_node")
								: child.data.gameStatus === "failed"
								? className.concat(" dead_node")
								: className}
							<div
								className={className}
							>{`{${child.data.state.Missionary}, ${child.data.state.Cannibal}, ${child.data.state.Boat}}`}</div>
						</ArcherElement>
						<div>{child.children.length !== 0 && Node(child.children)}</div>
						{/* {`{${node.data.state.Missionary}, ${node.data.state.Cannibal},
        ${node.data.state.Boat}}` && Recursive(nodes.children)} */}
					</div>
				))}
			</ArcherContainer>
		);
	}
}
