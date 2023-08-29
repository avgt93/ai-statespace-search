/* eslint-disable react/prop-types */
import { ArcherContainer, ArcherElement } from "react-archer";
import "./node.css";

const Node = (props) => {
	return (
		<div>
			<ArcherContainer strokeColor="black">
				<ArcherElement
					id="root"
					relations={[
						{
							targetId: "element1",
							targetAnchor: "top",
							sourceAnchor: "bottom",
							style: { strokeColor: "red", strokeWidth: 1 },
						},
						{
							targetId: "element2",
							targetAnchor: "top",
							sourceAnchor: "bottom",
							style: { strokeColor: "red", strokeWidth: 1 },
						},
						{
							targetId: "element3",
							targetAnchor: "top",
							sourceAnchor: "bottom",
							style: { strokeColor: "red", strokeWidth: 1 },
						},
						{
							targetId: "element4",
							targetAnchor: "top",
							sourceAnchor: "bottom",
							style: { strokeColor: "red", strokeWidth: 1 },
						},
						{
							targetId: "element5",
							targetAnchor: "top",
							sourceAnchor: "bottom",
							style: { strokeColor: "red", strokeWidth: 1 },
						},
					]}
				>
					<div className="node">(3,3,0)</div>
				</ArcherElement>
				<div className="baksa">
					<ArcherElement id="element1" relations={[{}]}>
						<div className="node">(2,3,1)</div>
					</ArcherElement>
					<ArcherElement id="element2" relations={[{}]}>
						<div className="node">(3,2,1)</div>
					</ArcherElement>
					<ArcherElement id="elemen3" relations={[{}]}>
						<div className="node">(1,3,1)</div>
					</ArcherElement>
					<ArcherElement
						id="element4"
						relations={[
							{
								targetId: "element5",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "red", strokeWidth: 1 },
							},
						]}
					>
						<div className="node">(3,1,1)</div>
					</ArcherElement>
					<ArcherElement id="elemen5" relations={[{}]}>
						<div className="node">(2,2,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement id="element6" relations={[{}]}>
						<div className="node">(3,2,0)</div>
					</ArcherElement>

					<ArcherElement id="element7" relations={[{}]}>
						<div className="node">(2,3,0)</div>
					</ArcherElement>
				</div>
			</ArcherContainer>
		</div>
	);
};

export default Node;
