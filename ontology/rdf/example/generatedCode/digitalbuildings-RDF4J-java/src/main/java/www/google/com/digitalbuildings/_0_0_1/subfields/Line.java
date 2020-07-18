package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Line 
* Refers to the incoming electrical feed (e.g. line current).
*/
@SuppressWarnings("serial")
public class Line extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ILine{

	IRI newInstance;
	public Line(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Line"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILine> getAllLinesObjectsCreated(){
		Set<ILine> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Line")).subjects().stream()
		.map(mapper->(ILine)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}