package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IEfficiency;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpecification;

public interface IEfficiency_percentage_specification extends IField{

	public IRI iri();

    public void addComposedOfEfficiency (IEfficiency parameter);

	public Set<IEfficiency> getComposedOfEfficiency();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfSpecification (ISpecification parameter);

	public Set<ISpecification> getComposedOfSpecification();

}