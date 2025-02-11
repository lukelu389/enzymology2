import React, { useEffect, useRef } from 'react';
import * as NGL from 'ngl';

const Protein3DView = ({ pdbFileUrl }) => {
    const stageRef = useRef(null);

    useEffect(() => {
        if (!stageRef.current) return;

        const stage = new NGL.Stage(stageRef.current);
        stage.setParameters({ backgroundColor: 'black' });

        // Load the dynamically fetched PDB file
        stage.loadFile(pdbFileUrl, { defaultRepresentation: true })
            .then((component) => {
                component.addRepresentation("cartoon", { colorScheme: "chainid" });
                stage.autoView();
            })
            .catch((error) => console.error("Error loading PDB file:", error));

        return () => stage.dispose();
    }, [pdbFileUrl]);

    return <div ref={stageRef} style={{ width: '100%', height: '500px', border: '1px solid #ccc' }} />;
};

export default Protein3DView;
