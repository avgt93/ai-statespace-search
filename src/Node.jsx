/* eslint-disable react/prop-types */
import { ArcherContainer, ArcherElement } from "react-archer";
import "./styles/node.css";

const Node = (props) => {
  return (
		<div className="div_main">
			<ArcherContainer strokeColor="black" noCurves={false} offset={2}>
				<div className="baksa">
					<ArcherElement
						id="start"
						relations={[
							{
								targetId: "element1",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,0)",
							},
							{
								targetId: "element2",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
							{
								targetId: "element3",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(2,0)",
							},
							{
								targetId: "element4",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,2)",
							},
							{
								targetId: "element5",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,1)",
							},
						]}
					>
						<div className="node">(3,3,0)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement id="element1" relations={[{}]}>
						<div className="node dead_node">(2,3,1)</div>
					</ArcherElement>
					<ArcherElement id="element2" relations={[{}]}>
						<div className="node">(3,2,1)</div>
					</ArcherElement>
					<ArcherElement id="element3" relations={[{}]}>
						<div className="node dead_node">(1,3,1)</div>
					</ArcherElement>
					<ArcherElement
						id="element4"
						relations={[
							{
								targetId: "element6",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
						]}
					>
						<div className="node">(3,1,1)</div>
					</ArcherElement>
					<ArcherElement
						id="element5"
						relations={[
							{
								targetId: "element7",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
						]}
					>
						<div className="node">(2,2,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element6"
						relations={[
							{
								targetId: "element8",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(2,0)",
							},
							{
								targetId: "element9",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,2)",
							},
							{
								targetId: "element10",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,1)",
							},
						]}
					>
						<div className="node">(3,2,0)</div>
					</ArcherElement>

					<ArcherElement id="element7" relations={[{}]}>
						<div className="node dead_node">(2,3,0)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement id="element8" relations={[{}]}>
						<div className="node dead_node">(1,2,1)</div>
					</ArcherElement>

					<ArcherElement
						id="element9"
						relations={[
							{
								targetId: "element11",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
						]}
					>
						<div className="node">(3,0,1)</div>
					</ArcherElement>
					<ArcherElement id="element10" relations={[{}]}>
						<div className="node dead_node">(2,1,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element11"
						relations={[
							{
								targetId: "element12",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(2,0)",
							},
							{
								targetId: "element13",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,1)",
							},
						]}
					>
						<div className="node">(3, 1, 0)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element12"
						relations={[
							{
								targetId: "element14",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,0)",
							},
							{
								targetId: "element15",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
							{
								targetId: "element16",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,2)",
							},
							{
								targetId: "element17",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,1)",
							},
						]}
					>
						<div className="node">(1,1,1)</div>
					</ArcherElement>
					<ArcherElement id="element13" relations={[{}]}>
						<div className="node dead_node">(2,0,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement id="element14" relations={[{}]}>
						<div className="node dead_node">(2,1,0)</div>
					</ArcherElement>
					<ArcherElement id="element15" relations={[{}]}>
						<div className="node dead_node">(1,2,0)</div>
					</ArcherElement>
					<ArcherElement id="element16" relations={[{}]}>
						<div className="node dead_node">(1,3,0)</div>
					</ArcherElement>
					<ArcherElement
						id="element17"
						relations={[
							{
								targetId: "element18",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(2,0)",
							},
						]}
					>
						<div className="node">(2,2,0)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element18"
						relations={[
							{
								targetId: "element19",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
						]}
					>
						<div className="node">(0,2,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element19"
						relations={[
							{
								targetId: "element20",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,2)",
							},
						]}
					>
						<div className="node">(0,3,0)</div>
					</ArcherElement>
				</div>

				<div className="baksa">
					<ArcherElement
						id="element20"
						relations={[
							{
								targetId: "element21",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,0)",
							},
							{
								targetId: "element22",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
						]}
					>
						<div className="node">(0,1,1)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement
						id="element21"
						relations={[
							{
								targetId: "element23",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,1)",
							},
							{
								targetId: "element24",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(1,1)",
							},
						]}
					>
						<div className="node">(1,1,0)</div>
					</ArcherElement>
					<ArcherElement
						id="element22"
						relations={[
							{
								targetId: "element24",
								targetAnchor: "top",
								sourceAnchor: "bottom",
								style: { strokeColor: "gray", strokeWidth: 1 },
								label: "(0,2)",
							},
						]}
					>
						<div className="node">(0,2,0)</div>
					</ArcherElement>
				</div>
				<div className="baksa">
					<ArcherElement id="element23" relations={[{}]}>
						<div className="node dead_node">(1,0,1)</div>
					</ArcherElement>
					<ArcherElement id="element24" relations={[{}]}>
						<div className="node won_node">(0,0,1)</div>
					</ArcherElement>
				</div>
			</ArcherContainer>
		</div>
	);
};

export default Node;
