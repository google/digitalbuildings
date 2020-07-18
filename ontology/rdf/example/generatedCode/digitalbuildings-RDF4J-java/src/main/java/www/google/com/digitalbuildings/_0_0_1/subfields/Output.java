package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Output 
* The output of a control loop (e.g. PID Loop Output)
*/
@SuppressWarnings("serial")
public class Output extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IOutput{

	IRI newInstance;
	public Output(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Output"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOutput> getAllOutputsObjectsCreated(){
		Set<IOutput> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Output")).subjects().stream()
		.map(mapper->(IOutput)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}