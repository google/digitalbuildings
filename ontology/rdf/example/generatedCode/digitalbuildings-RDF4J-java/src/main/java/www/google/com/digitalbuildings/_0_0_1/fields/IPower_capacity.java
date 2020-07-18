package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICapacity;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;

public interface IPower_capacity extends IField{

	public IRI iri();

    public void addComposedOfCapacity (ICapacity parameter);

	public Set<ICapacity> getComposedOfCapacity();

    public void addComposedOfPower (IPower parameter);

	public Set<IPower> getComposedOfPower();

}